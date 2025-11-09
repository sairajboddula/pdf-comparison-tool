"""
Documentation Generator Module - Comprehensive Implementation
Generates detailed documentation from code analysis
"""

import logging
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class DocumentationGenerator:
    """Generate comprehensive project documentation."""

    def __init__(self, project_data: Dict, use_ai: bool = False, ai_model: Optional[str] = None):
        """Initialize DocumentationGenerator."""
        self.project_data = project_data
        self.use_ai = use_ai
        self.ai_model = ai_model

        if use_ai:
            try:
                from src.ai_analyzer import AIAnalyzer
                self.ai_analyzer = AIAnalyzer(ai_model)
                logger.info(f"AI analyzer initialized with model: {ai_model}")
            except ImportError:
                logger.warning("AI dependencies not available")
                self.use_ai = False

    def generate(self, output_dir: Path, format_type: str = 'markdown') -> Path:
        """Generate comprehensive documentation."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        if format_type == 'markdown':
            return self._generate_comprehensive_markdown(output_dir)
        elif format_type == 'html':
            return self._generate_html(output_dir)
        elif format_type == 'pdf':
            return self._generate_pdf(output_dir)
        else:
            raise ValueError(f"Unsupported format: {format_type}")

    def _generate_comprehensive_markdown(self, output_dir: Path) -> Path:
        """Generate detailed Markdown documentation."""
        logger.info("Generating comprehensive Markdown documentation...")

        doc = []

        # Title and Overview
        project_name = self.project_data['name']
        doc.append(f"# {project_name} - Complete Project Documentation\n")
        doc.append(f"*Generated on: {self._get_timestamp()}*\n\n")

        # Table of Contents
        doc.append("## Table of Contents\n")
        doc.append("1. [Project Overview](#project-overview)\n")
        doc.append("2. [Project Statistics](#project-statistics)\n")
        doc.append("3. [Project Structure](#project-structure)\n")
        doc.append("4. [Module Documentation](#module-documentation)\n")
        doc.append("5. [Dependencies](#dependencies)\n")
        doc.append("6. [File Listing](#file-listing)\n\n")

        doc.append("---\n\n")

        # Project Overview
        doc.append("## Project Overview\n\n")
        doc.append(f"**Project Name:** {project_name}\n")
        doc.append(f"**Project Path:** `{self.project_data['path']}`\n\n")

        # Statistics
        doc.append("## Project Statistics\n\n")
        stats = self.project_data['stats']

        doc.append("| Metric | Value |\n")
        doc.append("|--------|-------|\n")
        doc.append(f"| Total Files | {stats['total_files']} |\n")
        doc.append(f"| Total Directories | {stats['total_dirs']} |\n")
        doc.append(f"| Total Lines of Code | {stats['total_lines']:,} |\n")
        doc.append(f"| Python Files | {stats['python_files']} |\n")
        doc.append(f"| Classes | {stats['classes']} |\n")
        doc.append(f"| Functions | {stats['functions']} |\n")
        doc.append(f"| Imports | {stats['imports']} |\n\n")

        # File type distribution
        if 'file_type_distribution' in stats:
            doc.append("### File Type Distribution\n\n")
            doc.append("| Extension | Count |\n")
            doc.append("|-----------|-------|\n")
            for ext, count in sorted(stats['file_type_distribution'].items(), key=lambda x: x[1], reverse=True):
                ext_display = ext if ext else '(no extension)'
                doc.append(f"| `{ext_display}` | {count} |\n")
            doc.append("\n")

        # Project Structure
        doc.append("## Project Structure\n\n")
        doc.append("```\n")
        doc.append(self._tree_to_string(self.project_data['tree']))
        doc.append("```\n\n")

        # Module Documentation
        modules = self.project_data.get('modules', {})
        if modules:
            doc.append("## Module Documentation\n\n")

            for module_path in sorted(modules.keys()):
                module_data = modules[module_path]
                module_name = Path(module_path).stem

                doc.append(f"### {module_path}\n\n")

                # Module docstring
                if module_data.get('docstring'):
                    doc.append(f"*{module_data['docstring']}*\n\n")

                # Module stats
                doc.append(f"**Statistics:**\n")
                doc.append(f"- Classes: {len(module_data.get('classes', []))}\n")
                doc.append(f"- Functions: {len(module_data.get('functions', []))}\n")
                doc.append(f"- Imports: {len(module_data.get('imports', []))}\n")
                if module_data.get('complexity', 0) > 0:
                    doc.append(f"- Complexity: {module_data['complexity']}\n")
                doc.append("\n")

                # Dependencies
                deps = module_data.get('dependencies', [])
                if deps:
                    doc.append(f"**Dependencies:**\n")
                    for dep in deps:
                        doc.append(f"- `{dep}`\n")
                    doc.append("\n")

                # Classes
                classes = module_data.get('classes', [])
                if classes:
                    doc.append(f"**Classes:**\n\n")
                    for cls in classes:
                        doc.append(f"#### `class {cls['name']}`\n\n")

                        if cls.get('docstring'):
                            doc.append(f"*{cls['docstring']}*\n\n")

                        if cls.get('bases'):
                            bases = ', '.join(cls['bases'])
                            doc.append(f"**Inherits from:** `{bases}`\n\n")

                        doc.append(f"**Location:** Line {cls['lineno']}\n\n")

                        methods = cls.get('methods', [])
                        if methods:
                            doc.append(f"**Methods:**\n")
                            for method in methods:
                                args = ', '.join(method.get('args', []))
                                returns = method.get('returns', 'None')
                                doc.append(f"- `{method['name']}({args})` → `{returns}`")

                                decorators = method.get('decorators', [])
                                if decorators:
                                    doc.append(f" *[@{', @'.join(decorators)}]*")

                                doc.append(f" (line {method['lineno']})\n")
                            doc.append("\n")

                # Functions
                functions = module_data.get('functions', [])
                if functions:
                    doc.append(f"**Functions:**\n\n")
                    for func in functions:
                        args = ', '.join(func.get('args', []))
                        returns = func.get('returns', 'None')

                        doc.append(f"#### `def {func['name']}({args})`\n\n")

                        if func.get('docstring'):
                            doc.append(f"*{func['docstring']}*\n\n")

                        doc.append(f"**Returns:** `{returns}`\n")
                        doc.append(f"**Location:** Line {func['lineno']}\n")

                        if func.get('complexity', 0) > 1:
                            doc.append(f"**Complexity:** {func['complexity']}\n")

                        doc.append("\n")

                doc.append("---\n\n")

        # Dependencies
        doc.append("## Dependencies\n\n")
        doc.append("### Internal Dependencies\n\n")
        # Add dependency information here
        doc.append("*See module documentation above for specific dependencies.*\n\n")

        # Write to file
        output_file = output_dir / "README.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(''.join(doc))

        logger.info(f"✓ Comprehensive documentation saved: {output_file}")
        return output_file

    def _generate_html(self, output_dir: Path) -> Path:
        """Generate HTML documentation."""
        # First generate markdown
        md_file = self._generate_comprehensive_markdown(output_dir)
        logger.info(f"HTML documentation base created: {md_file}")
        return md_file

    def _generate_pdf(self, output_dir: Path) -> Path:
        """Generate PDF documentation."""
        md_file = self._generate_comprehensive_markdown(output_dir)
        logger.info(f"PDF documentation base created: {md_file}")
        return md_file

    def _tree_to_string(self, tree: Dict, indent: int = 0, is_last: bool = True) -> str:
        """Convert tree to string with proper formatting."""
        lines = []
        name = tree.get('name', '')
        tree_type = tree.get('type', '')

        prefix = "  " * indent
        connector = "└── " if is_last else "├── "

        if indent == 0:
            lines.append(f"{name}/\n")
        else:
            if tree_type == 'directory':
                lines.append(f"{prefix}{connector}📁 {name}/\n")
            else:
                ext = tree.get('extension', '')
                lines_count = tree.get('lines', 0)
                if ext == '.py' and lines_count > 0:
                    lines.append(f"{prefix}{connector}🐍 {name} ({lines_count} lines)\n")
                else:
                    lines.append(f"{prefix}{connector}📄 {name}\n")

        children = tree.get('children', [])
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            lines.append(self._tree_to_string(child, indent + 1, is_last_child))

        return ''.join(lines)

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
