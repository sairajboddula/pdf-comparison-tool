"""
Professional Workflow Diagram Generator - PRODUCTION GRADE
==========================================================
Creates clean, hierarchical, enterprise-grade workflow diagrams
"""

import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple
import graphviz
from collections import defaultdict

logger = logging.getLogger(__name__)


class ProfessionalWorkflowGenerator:
    """Generate production-grade professional workflow diagrams."""

    def __init__(self, project_data: Dict, theme: str = 'default'):
        """Initialize workflow generator."""
        self.project_data = project_data
        self.theme = theme
        self.colors = self._get_theme_colors()

    def _get_theme_colors(self) -> Dict:
        """Professional color schemes."""
        themes = {
            'default': {
                'bg': '#F8F9FA',
                'cluster_bg': '#E8F4F8',
                'cluster_border': '#2C3E50',
                'entry_point': '#E74C3C',  # Red
                'leaf_module': '#3498DB',  # Blue
                'regular_module': '#2ECC71',  # Green
                'module_text': 'white',
                'edge_color': '#34495E',
                'edge_weight': '#BDC3C7'
            },
            'dark': {
                'bg': '#1E1E1E',
                'cluster_bg': '#2D3E50',
                'cluster_border': '#ECF0F1',
                'entry_point': '#E74C3C',
                'leaf_module': '#3498DB',
                'regular_module': '#2ECC71',
                'module_text': 'white',
                'edge_color': '#ECF0F1',
                'edge_weight': '#7F8C8D'
            },
            'corporate': {
                'bg': 'white',
                'cluster_bg': '#F5F7FA',
                'cluster_border': '#1A5490',
                'entry_point': '#C23C2A',
                'leaf_module': '#0066CC',
                'regular_module': '#008000',
                'module_text': 'white',
                'edge_color': '#333333',
                'edge_weight': '#999999'
            }
        }
        return themes.get(self.theme, themes['default'])

    def generate_professional_workflow(self, output_path: Path) -> Path:
        """Generate production-grade professional workflow diagram."""
        logger.info("Creating PRODUCTION-GRADE professional workflow diagram...")

        # Use 'dot' engine for hierarchical layout (perfect for workflows)
        dot = graphviz.Digraph(
            name='ProfessionalWorkflow',
            format='svg',
            engine='dot'  # Hierarchical layout
        )

        # Global graph settings
        dot.attr(
            rankdir='TB',  # Top to bottom
            bgcolor=self.colors['bg'],
            fontname='Segoe UI, Arial',
            fontsize='10',
            nodesep='1.2',
            ranksep='1.5',
            splines='ortho',  # Proper edges
            concentrate='false',
            compound='true'
        )

        # Node defaults
        dot.attr('node',
            shape='box',
            style='filled,rounded',
            fontname='Segoe UI, Arial',
            fontsize='11',
            margin='0.5,0.3',
            penwidth='2.5',
            fillcolor=self.colors['regular_module'],
            fontcolor=self.colors['module_text']
        )

        # Edge defaults
        dot.attr('edge',
            color=self.colors['edge_color'],
            penwidth='2',
            arrowsize='1.2',
            fontname='Segoe UI, Arial',
            fontsize='9'
        )

        modules = self.project_data.get('modules', {})
        if not modules:
            logger.warning("No modules found")
            return output_path

        # Analyze modules
        workflow_data = self.project_data.get('workflow_data', {})
        dependencies = workflow_data.get('dependencies', {})
        entry_points = workflow_data.get('entry_points', [])
        leaf_modules = dependencies.get('leaf_modules', [])
        hierarchy = workflow_data.get('hierarchy', {})

        # Build layers for hierarchical display
        layers = self._build_hierarchy_layers(
            modules,
            entry_points,
            leaf_modules,
            dependencies
        )

        # Create subgraph for each layer
        layer_nodes = {}
        for layer_idx, layer_modules in enumerate(layers):
            if layer_modules:
                with dot.subgraph(name=f'cluster_layer_{layer_idx}') as cluster:
                    cluster.attr(
                        label=f'Layer {layer_idx + 1}',
                        style='filled,rounded',
                        fillcolor=self.colors['cluster_bg'],
                        color=self.colors['cluster_border'],
                        fontcolor=self.colors['cluster_border'],
                        penwidth='2',
                        fontsize='12',
                        fontname='Segoe UI, Arial'
                    )

                    for module_path in layer_modules:
                        node_id = module_path.replace('/', '_').replace('.', '_')
                        layer_nodes[module_path] = node_id

                        module_data = modules.get(module_path, {})
                        module_name = Path(module_path).stem

                        # Determine node color
                        if module_path in entry_points:
                            node_color = self.colors['entry_point']
                            icon = '🚀'
                        elif module_path in leaf_modules:
                            node_color = self.colors['leaf_module']
                            icon = '🎯'
                        else:
                            node_color = self.colors['regular_module']
                            icon = '📦'

                        # Build label
                        classes = len(module_data.get('classes', []))
                        functions = len(module_data.get('functions', []))
                        imports = len(module_data.get('imports', []))

                        label = f"{icon} {module_name}"
                        label += f"\n{'─' * 20}"
                        label += f"\n🏛️  {classes} Classes | ⚙️  {functions} Funcs"
                        if imports > 0:
                            label += f"\n📥 {imports} Imports"

                        cluster.node(
                            node_id,
                            label=label,
                            fillcolor=node_color,
                            fontcolor=self.colors['module_text'],
                            shape='box',
                            style='filled,rounded'
                        )

        # Add edges with smart filtering
        self._add_professional_edges(dot, modules, layer_nodes, entry_points)

        # Add legend
        self._add_professional_legend(dot)

        # Render
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        dot.render(
            filename=output_path.stem,
            directory=output_path.parent,
            cleanup=True
        )

        logger.info(f"✓ Professional workflow diagram saved: {output_path}")
        return output_path

    def _build_hierarchy_layers(self, modules, entry_points, leaf_modules, dependencies):
        """Build hierarchical layers for workflow display."""
        layers = []
        processed = set()

        # Layer 1: Entry points
        if entry_points:
            layer = [ep for ep in entry_points if ep in modules]
            layers.append(layer)
            processed.update(layer)

        # Layer 2: Modules with dependencies
        dependent_modules = []
        for module_path in modules.keys():
            if module_path not in processed:
                if module_path not in leaf_modules:
                    dependent_modules.append(module_path)

        if dependent_modules:
            layers.append(dependent_modules)
            processed.update(dependent_modules)

        # Layer 3: Leaf modules
        if leaf_modules:
            leaf = [lm for lm in leaf_modules if lm in modules and lm not in processed]
            if leaf:
                layers.append(leaf)
                processed.update(leaf)

        return layers

    def _add_professional_edges(self, dot, modules, layer_nodes, entry_points):
        """Add professional edges showing relationships."""
        edges_added = set()

        for module_path, module_data in modules.items():
            if module_path not in layer_nodes:
                continue

            source_id = layer_nodes[module_path]
            deps = module_data.get('dependencies', [])[:5]  # Limit to 5

            for dep in deps:
                for target_module in modules.keys():
                    if target_module not in layer_nodes:
                        continue

                    if dep in target_module.replace('/', '.').replace('.py', ''):
                        target_id = layer_nodes[target_module]
                        edge_key = (source_id, target_id)

                        if edge_key not in edges_added:
                            # Determine edge color based on source
                            if module_path in entry_points:
                                edge_color = self.colors['entry_point']
                                penwidth = '2.5'
                            else:
                                edge_color = self.colors['edge_color']
                                penwidth = '2'

                            dot.edge(
                                source_id,
                                target_id,
                                color=edge_color,
                                penwidth=penwidth,
                                arrowsize='1.5'
                            )
                            edges_added.add(edge_key)
                        break

    def _add_professional_legend(self, dot):
        """Add professional legend."""
        with dot.subgraph(name='cluster_legend') as legend:
            legend.attr(
                label='Legend',
                style='filled,rounded',
                fillcolor=self.colors['cluster_bg'],
                color=self.colors['cluster_border'],
                penwidth='2'
            )

            legend.node(
                'legend_entry',
                '🚀 Entry Point',
                fillcolor=self.colors['entry_point'],
                fontcolor='white',
                shape='box',
                style='filled,rounded'
            )
            legend.node(
                'legend_regular',
                '📦 Regular Module',
                fillcolor=self.colors['regular_module'],
                fontcolor='white',
                shape='box',
                style='filled,rounded'
            )
            legend.node(
                'legend_leaf',
                '🎯 Leaf Module',
                fillcolor=self.colors['leaf_module'],
                fontcolor='white',
                shape='box',
                style='filled,rounded'
            )

            # Invisible edges to stack legend items
            legend.edge('legend_entry', 'legend_regular', style='invis')
            legend.edge('legend_regular', 'legend_leaf', style='invis')
