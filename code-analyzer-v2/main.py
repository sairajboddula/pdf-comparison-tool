#!/usr/bin/env python3
"""
AI-Powered Code Analyzer - Main Entry Point
============================================
Version: 2.0 - COMPLETE IMPLEMENTATION
"""

import argparse
import logging
import sys
from pathlib import Path
import yaml
import traceback

from src.scanner import ProjectScanner
from src.diagram_generator import DiagramGenerator
from src.workflow_analyzer import WorkflowAnalyzer
from src.professional_workflow_generator_v2 import ProfessionalWorkflowGenerator
from src.animator import FlowAnimator
from src.doc_generator import DocumentationGenerator
from src.utils import setup_logging, validate_path, print_banner



def load_config(config_path: str = 'config.yaml') -> dict:
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.warning(f"Config file {config_path} not found. Using defaults.")
        return {}


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description='AI-Powered Code Structure Analyzer v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py -p ./my_project --all
  python main.py -p ./my_project -d architecture --theme colorful
  python main.py -p ./my_project --docs --use-ai
        """
    )

    parser.add_argument('-p', '--project_path', type=str, required=True,
                       help='Path to the project directory to analyze')
    parser.add_argument('-d', '--diagram', type=str, 
                       choices=['architecture', 'workflow', 'animated', 'all'],
                       default='all', help='Type of diagram (default: all)')
    parser.add_argument('-o', '--output', type=str, default='./outputs',
                       help='Output directory (default: ./outputs)')
    parser.add_argument('-f', '--format', type=str, 
                       choices=['svg', 'png', 'pdf'], default='svg',
                       help='Output format (default: svg)')
    parser.add_argument('--depth', type=int, default=-1,
                       help='Max directory depth (-1 = unlimited)')
    parser.add_argument('--exclude', type=str, nargs='+',
                       default=['__pycache__', '.git', '.venv', 'venv', 'node_modules'],
                       help='Directories to exclude')
    parser.add_argument('--include-hidden', action='store_true',
                       help='Include hidden files')
    parser.add_argument('--docs', action='store_true',
                       help='Generate documentation')
    parser.add_argument('--docs-only', action='store_true',
                       help='Only generate documentation')
    parser.add_argument('--docs-format', type=str,
                       choices=['markdown', 'html', 'pdf'], default='markdown')
    parser.add_argument('--animation-fps', type=int, default=2)
    parser.add_argument('--animation-duration', type=float, default=0.5)
    parser.add_argument('--use-ai', action='store_true',
                       help='Use AI for analysis')
    parser.add_argument('--ai-model', type=str, default='bert-base-uncased')
    parser.add_argument('--theme', type=str,
                       choices=['default', 'dark', 'colorful', 'minimal'], default='default')
    parser.add_argument('--icons', action='store_true',
                       help='Use icons in diagrams')
    parser.add_argument('--all', action='store_true',
                       help='Generate all outputs')
    parser.add_argument('--show-imports', action='store_true',
                       help='Show import relationships in diagrams')
    parser.add_argument('--show-calls', action='store_true',
                       help='Show function call relationships')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                       help='Increase verbosity')
    parser.add_argument('--config', type=str, default='config.yaml')

    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()

    # Setup logging
    log_level = logging.WARNING
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG

    # setup_logging(log_level)
    logger = setup_logging(logging.INFO)

    print_banner()
    logger.info("AI-Powered Code Analyzer v2.0 Starting...")

    # Load configuration
    config = load_config(args.config)

    # Validate project path
    project_path = Path(args.project_path)
    if not validate_path(project_path):
        logger.error(f"Invalid project path: {project_path}")
        sys.exit(1)

    # Create output directory
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {output_path}")

    try:
        # Step 1: Comprehensive project scanning
        logger.info("\n" + "="*60)
        logger.info("[1/5] Scanning project structure...")
        logger.info("="*60)

        scanner = ProjectScanner(
            project_path,
            max_depth=args.depth,
            exclude_dirs=args.exclude,
            include_hidden=args.include_hidden,
            analyze_imports=args.show_imports,
            analyze_calls=args.show_calls
        )
        project_data = scanner.scan()

        # Print statistics
        stats = project_data['stats']
        logger.info(f"✓ Found {stats['total_files']} files in {stats['total_dirs']} directories")
        logger.info(f"✓ Python files: {stats['python_files']}")
        logger.info(f"✓ Total lines: {stats['total_lines']:,}")
        logger.info(f"✓ Classes: {stats['classes']}, Functions: {stats['functions']}")

        generate_diagrams = not args.docs_only
        generate_docs = args.docs or args.all or args.docs_only
        generate_all = args.all or args.diagram == 'all'

        if generate_diagrams:
            # Step 2: Generate architecture diagram
            if generate_all or args.diagram == 'architecture':
                logger.info("\n" + "="*60)
                logger.info("[2/5] Generating architecture diagram...")
                logger.info("="*60)

                diagram_gen = DiagramGenerator(
                    project_data,
                    theme=args.theme,
                    use_icons=args.icons,
                    output_format=args.format,
                    show_imports=args.show_imports
                )
                arch_file = diagram_gen.generate_architecture_diagram(
                    output_path / f"architecture.{args.format}"
                )
                logger.info(f"✓ Architecture diagram saved: {arch_file}")

            # Step 3: Generate workflow diagram
            if generate_all or args.diagram == 'workflow':
                logger.info("\\n" + "="*60)
                logger.info("[3/5] Generating professional workflow diagram...")
                logger.info("="*60)
                
                workflow_analyzer = WorkflowAnalyzer(project_data)
                workflow_data = workflow_analyzer.analyze()
                
                # Store workflow data
                project_data['workflow_data'] = workflow_data
                
                # Use production-grade generator
                from src.professional_workflow_generator_v2 import ProfessionalWorkflowGenerator
                
                workflow_gen = ProfessionalWorkflowGenerator(
                    project_data,
                    theme=args.theme
                )
                
                workflow_file = workflow_gen.generate_professional_workflow(
                    output_path / f"workflow.{args.format}"
                )
                logger.info(f"✓ Professional workflow diagram saved: {workflow_file}")

            

            # Step 4: Generate animated flowchart
            if generate_all or args.diagram == 'animated':
                logger.info("\n" + "="*60)
                logger.info("[4/5] Generating animated flowchart...")
                logger.info("="*60)

                animator = FlowAnimator(
                    project_data,
                    fps=args.animation_fps,
                    duration=args.animation_duration,
                    theme=args.theme
                )
                anim_file = animator.create_animated_flowchart(
                    output_path / "animated_flow.gif"
                )
                logger.info(f"✓ Animated flowchart saved: {anim_file}")

        # Step 5: Generate documentation
        # if generate_docs:
        #     logger.info("\n" + "="*60)
        #     logger.info("[5/5] Generating documentation...")
        #     logger.info("="*60)

        #     doc_gen = DocumentationGenerator(
        #         project_data,
        #         use_ai=args.use_ai,
        #         ai_model=args.ai_model if args.use_ai else None
        #     )
        #     doc_file = doc_gen.generate(
        #         output_path / "documentation",
        #         format_type=args.docs_format
        #     )
        #     logger.info(f"✓ Documentation generated: {doc_file}")

        if generate_docs:
            logger.info("Generating AI-enhanced documentation...")
            
            from src.ai_documentation_generator import AIDocumentationGenerator
            
            ai_doc_gen = AIDocumentationGenerator(use_ai=True)
            
            doc_file = ai_doc_gen.generate_comprehensive_docs(
                project_data,
                output_path / "documentation"
            )
            api_file = ai_doc_gen.generate_api_documentation(
                project_data,
                output_path / "documentation"
            )
            logger.info(f"✓ Comprehensive documentation saved: {doc_file}")
            logger.info(f"✓ API documentation saved: {api_file}")


        # Final summary
        logger.info("\n" + "="*60)
        logger.info("✓ ANALYSIS COMPLETE!")
        logger.info("="*60)
        logger.info(f"\nOutput location: {output_path.absolute()}")
        logger.info("\nGenerated files:")

        for file in output_path.rglob('*'):
            if file.is_file():
                logger.info(f"  • {file.relative_to(output_path)}")

    except Exception as e:
        logger.error(f"\n❌ Error during analysis: {e}")
        logger.debug(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
