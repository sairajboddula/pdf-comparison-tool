"""
AI-Powered Documentation Generator - Using Open Source Models
============================================================
Generates professional, clean documentation using Hugging Face transformers
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional
import json

logger = logging.getLogger(__name__)

# Try to import transformers (optional, graceful fallback)
try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False
    logger.warning("Transformers not installed. Using template-based documentation.")


class AIDocumentationGenerator:
    """Generate professional documentation using open-source AI."""

    def __init__(self, use_ai: bool = True, model_name: str = "facebook/bart-large-cnn"):
        """Initialize AI documentation generator.

        Args:
            use_ai: Whether to use AI for generation
            model_name: HuggingFace model to use
        """
        self.use_ai = use_ai and HAS_TRANSFORMERS
        self.model_name = model_name
        self.summarizer = None

        if self.use_ai:
            try:
                logger.info(f"Loading AI model: {model_name}")
                self.summarizer = pipeline(
                    "summarization",
                    model=model_name,
                    device=-1  # CPU mode
                )
                logger.info("✓ AI model loaded successfully")
            except Exception as e:
                logger.warning(f"Failed to load AI model: {e}. Using templates.")
                self.use_ai = False

    def generate_module_documentation(self, module_path: str, module_data: Dict) -> str:
        """Generate documentation for a module using AI."""

        if not module_data:
            return f"## {module_path}\n\nNo data available.\n"

        doc = f"## {module_path}\n\n"

        # Module docstring
        docstring = module_data.get('docstring', '')
        if docstring:
            if self.use_ai:
                summary = self._summarize(docstring, max_length=100, min_length=30)
            else:
                summary = docstring[:200]
            doc += f"**Purpose:** {summary}\n\n"

        # Statistics
        classes = module_data.get('classes', [])
        functions = module_data.get('functions', [])
        imports = module_data.get('imports', [])

        doc += f"**Statistics:**\n"
        doc += f"- 🏛️ Classes: {len(classes)}\n"
        doc += f"- ⚙️ Functions: {len(functions)}\n"
        doc += f"- 📥 Imports: {len(imports)}\n"
        doc += f"- 📊 Lines of Code: {module_data.get('lines', 0)}\n\n"

        # Classes documentation
        if classes:
            doc += "### Classes\n\n"
            for cls in classes:
                doc += self._generate_class_docs(cls)

        # Functions documentation
        if functions:
            doc += "### Functions\n\n"
            for func in functions:
                doc += self._generate_function_docs(func)

        # Dependencies
        if imports:
            doc += "### Dependencies\n\n"
            for imp in imports[:10]:  # Limit to 10
                doc += f"- `{imp}`\n"
            if len(imports) > 10:
                doc += f"- ... and {len(imports) - 10} more\n"
            doc += "\n"

        return doc

    def _generate_class_docs(self, cls: Dict) -> str:
        """Generate documentation for a class."""
        doc = f"#### `class {cls['name']}`\n\n"

        # Class docstring
        if cls.get('docstring'):
            if self.use_ai:
                summary = self._summarize(cls['docstring'], max_length=80, min_length=20)
            else:
                summary = cls['docstring'][:150]
            doc += f"*{summary}*\n\n"

        # Base classes
        if cls.get('bases'):
            bases = ', '.join(cls['bases'])
            doc += f"**Inherits from:** `{bases}`\n\n"

        # Location
        doc += f"**Location:** Line {cls['lineno']}\n\n"

        # Methods
        methods = cls.get('methods', [])
        if methods:
            doc += f"**Methods ({len(methods)}):**\n"
            for method in methods[:5]:  # Show top 5
                args = ', '.join(method.get('args', []))
                returns = method.get('returns', 'None')
                decorators = method.get('decorators', [])
                decorator_str = f" [@{', @'.join(decorators)}]" if decorators else ""
                doc += f"- `{method['name']}({args})` → `{returns}`{decorator_str}\n"

            if len(methods) > 5:
                doc += f"- ... and {len(methods) - 5} more methods\n"
            doc += "\n"

        return doc

    def _generate_function_docs(self, func: Dict) -> str:
        """Generate documentation for a function."""
        args = ', '.join(func.get('args', []))
        returns = func.get('returns', 'None')

        doc = f"#### `def {func['name']}({args})`\n\n"

        # Function docstring
        if func.get('docstring'):
            if self.use_ai:
                summary = self._summarize(func['docstring'], max_length=100, min_length=20)
            else:
                summary = func['docstring'][:200]
            doc += f"*{summary}*\n\n"

        # Details
        doc += f"**Returns:** `{returns}`\n"
        doc += f"**Location:** Line {func['lineno']}\n"

        if func.get('complexity', 0) > 1:
            doc += f"**Complexity:** {func['complexity']}\n"

        doc += "\n"
        return doc

    def _summarize(self, text: str, max_length: int = 150, min_length: int = 30) -> str:
        """Summarize text using AI."""
        if not self.use_ai or not self.summarizer or not text:
            return text[:max_length]

        try:
            # Truncate very long texts
            if len(text) > 1024:
                text = text[:1024]

            summary = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )

            return summary[0]['summary_text'].strip()
        except Exception as e:
            logger.debug(f"Summarization failed: {e}")
            return text[:max_length]

    def generate_comprehensive_docs(
        self,
        project_data: Dict,
        output_dir: Path
    ) -> Path:
        """Generate comprehensive AI-enhanced documentation."""

        logger.info("Generating AI-enhanced comprehensive documentation...")

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        modules = project_data.get('modules', {})
        stats = project_data.get('stats', {})

        doc = []

        # Title
        project_name = project_data.get('name', 'Project')
        doc.append(f"# {project_name} - AI-Enhanced Documentation\n\n")
        doc.append(f"*Generated with AI-powered analysis*\n\n")

        # Quick Stats
        doc.append("## 📊 Project Statistics\n\n")
        doc.append(f"| Metric | Value |\n")
        doc.append(f"|--------|-------|\n")
        doc.append(f"| Total Files | {stats.get('total_files', 0)} |\n")
        doc.append(f"| Python Files | {stats.get('python_files', 0)} |\n")
        doc.append(f"| Total Lines | {stats.get('total_lines', 0):,} |\n")
        doc.append(f"| Classes | {stats.get('classes', 0)} |\n")
        doc.append(f"| Functions | {stats.get('functions', 0)} |\n")
        doc.append(f"| Modules | {len(modules)} |\n\n")

        # Table of Contents
        doc.append("## 📑 Table of Contents\n\n")
        for i, module_path in enumerate(sorted(modules.keys()), 1):
            module_name = Path(module_path).stem
            doc.append(f"{i}. [{module_name}](#{module_name.lower()})\n")
        doc.append("\n")

        # Module Documentation
        doc.append("## 📚 Module Documentation\n\n")

        for module_path in sorted(modules.keys()):
            module_data = modules[module_path]
            module_doc = self.generate_module_documentation(module_path, module_data)
            doc.append(module_doc)
            doc.append("---\n\n")

        # Generate Architecture Overview
        doc.append("## 🏗️ Architecture Overview\n\n")
        doc.append("### Module Dependencies\n\n")

        dependencies = project_data.get('workflow_data', {}).get('dependencies', {})
        if dependencies:
            internal_deps = dependencies.get('internal', {})
            external_deps = dependencies.get('external', {})

            if internal_deps:
                doc.append("**Internal Dependencies:**\n\n")
                for module, deps in list(internal_deps.items())[:5]:
                    if deps:
                        doc.append(f"- `{module}` → {', '.join(deps)}\n")

            if external_deps:
                doc.append("\n**External Dependencies:**\n\n")
                external_set = set()
                for deps in external_deps.values():
                    external_set.update(deps)

                for ext_dep in sorted(list(external_set))[:10]:
                    doc.append(f"- `{ext_dep}`\n")

        # Write documentation
        doc_file = output_dir / "README.md"
        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write(''.join(doc))

        logger.info(f"✓ AI-enhanced documentation generated: {doc_file}")
        return doc_file

    def generate_api_documentation(self, project_data: Dict, output_dir: Path) -> Path:
        """Generate detailed API documentation."""

        logger.info("Generating detailed API documentation...")

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        modules = project_data.get('modules', {})

        api_doc = []
        api_doc.append("# API Reference\n\n")
        api_doc.append("Complete API documentation for all modules and classes.\n\n")

        for module_path in sorted(modules.keys()):
            module_data = modules[module_path]
            api_doc.append(f"## `{module_path}`\n\n")

            # Classes
            for cls in module_data.get('classes', []):
                api_doc.append(f"### class `{cls['name']}`\n\n")

                if cls.get('docstring'):
                    if self.use_ai:
                        summary = self._summarize(cls['docstring'])
                    else:
                        summary = cls['docstring']
                    api_doc.append(f"{summary}\n\n")

                # Methods
                for method in cls.get('methods', []):
                    args_str = ', '.join(method.get('args', []))
                    api_doc.append(f"**`{method['name']}({args_str})`**\n\n")
                    if method.get('docstring'):
                        if self.use_ai:
                            summary = self._summarize(method['docstring'], max_length=100, min_length=20)
                        else:
                            summary = method['docstring'][:200]
                        api_doc.append(f"{summary}\n\n")

            # Functions
            for func in module_data.get('functions', []):
                args_str = ', '.join(func.get('args', []))
                api_doc.append(f"### `{func['name']}({args_str})`\n\n")
                if func.get('docstring'):
                    if self.use_ai:
                        summary = self._summarize(func['docstring'])
                    else:
                        summary = func['docstring']
                    api_doc.append(f"{summary}\n\n")

            api_doc.append("---\n\n")

        # Write API docs
        api_file = output_dir / "API.md"
        with open(api_file, 'w', encoding='utf-8') as f:
            f.write(''.join(api_doc))

        logger.info(f"✓ API documentation generated: {api_file}")
        return api_file
