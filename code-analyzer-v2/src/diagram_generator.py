"""
Diagram Generator Module - PROFESSIONAL IMPLEMENTATION
======================================================
Creates clean, professional diagrams with icons and proper styling
"""

import logging
from pathlib import Path
from typing import Dict, Optional, List
import graphviz
from collections import defaultdict

logger = logging.getLogger(__name__)


class DiagramGenerator:
    """Generate professional, clean diagrams."""

    def __init__(
        self,
        project_data: Dict,
        theme: str = 'default',
        use_icons: bool = True,
        output_format: str = 'svg',
        show_imports: bool = True
    ):
        """Initialize with comprehensive options."""
        self.project_data = project_data
        self.theme = theme
        self.use_icons = use_icons
        self.output_format = output_format
        self.show_imports = show_imports

        self.colors = self._get_theme_colors()

    def _get_theme_colors(self) -> Dict:
        """Get colors for the selected theme."""
        themes = {
            'default': {
                'bg': 'white',
                'root_module': '#FF6B6B',
                'regular_module': '#4ECDC4',
                'leaf_module': '#45B7D1',
                'internal_dep': '#95E1D3',
                'external_dep': '#F38181',
                'text': '#2C3E50',
                'text_light': 'white',
                'border': '#34495E',
                'cluster_border': '#7F8C8D',
                'accent': '#F39C12'
            },
            'dark': {
                'bg': '#1E1E1E',
                'root_module': '#FF6B6B',
                'regular_module': '#4ECDC4',
                'leaf_module': '#45B7D1',
                'internal_dep': '#95E1D3',
                'external_dep': '#FF8A8A',
                'text': '#ECF0F1',
                'text_light': 'white',
                'border': '#95A5A6',
                'cluster_border': '#7F8C8D',
                'accent': '#F39C12'
            },
            'colorful': {
                'bg': 'white',
                'root_module': '#FF6B6B',
                'regular_module': '#4ECDC4',
                'leaf_module': '#95E1D3',
                'internal_dep': '#FFE66D',
                'external_dep': '#A8E6CF',
                'text': '#333333',
                'text_light': 'white',
                'border': '#FF8B94',
                'cluster_border': '#FFB6C1',
                'accent': '#FF6B9D'
            },
            'minimal': {
                'bg': 'white',
                'root_module': '#555555',
                'regular_module': '#888888',
                'leaf_module': '#AAAAAA',
                'internal_dep': '#CCCCCC',
                'external_dep': '#999999',
                'text': '#333333',
                'text_light': 'white',
                'border': '#666666',
                'cluster_border': '#DDDDDD',
                'accent': '#444444'
            }
        }
        return themes.get(self.theme, themes['default'])

    def generate_architecture_diagram(self, output_path: Path) -> Path:
        """Generate comprehensive architecture diagram."""
        logger.info("Creating professional architecture diagram...")

        dot = graphviz.Digraph(
            name='Architecture',
            format=self.output_format
        )

        dot.attr(
            rankdir='TB',
            splines='ortho',
            bgcolor=self.colors['bg'],
            fontname='Helvetica',
            fontsize='10',
            overlap='false',
            nodesep='0.6',
            ranksep='1.0'
        )

        dot.attr('node',
            shape='box',
            style='filled,rounded',
            fontname='Helvetica',
            fontsize='9',
            margin='0.3,0.15',
            penwidth='2'
        )

        dot.attr('edge',
            color=self.colors['cluster_border'],
            penwidth='1.5'
        )

        stats = self.project_data['stats']
        dot.node(
            'root',
            label=self.project_data['name'],
            fillcolor=self.colors['root_module'],
            shape='box',
            fontcolor=self.colors['text_light'],
            fontsize='12',
            penwidth='3'
        )

        self._add_architecture_nodes(dot, self.project_data['tree'], 'root', depth=0)
        self._add_professional_legend(dot)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        dot.render(filename=output_path.stem, directory=output_path.parent, cleanup=True)
        logger.info(f"✓ Professional architecture diagram saved")
        return output_path

    def _add_architecture_nodes(self, dot, tree, parent_id, depth, max_depth=3):
        """Add architecture nodes."""
        if depth > max_depth:
            return

        for i, child in enumerate(tree.get('children', [])):
            child_type = child.get('type')
            child_name = child.get('name', '')
            node_id = f"{parent_id}_{i}"

            if child_type == 'directory':
                count = len(child.get('children', []))
                label = f"{child_name}/\n({count})"
                dot.node(node_id, label=label, fillcolor=self.colors['regular_module'],
                        shape='folder', fontcolor=self.colors['text_light'])
                dot.edge(parent_id, node_id, arrowhead='none')
                self._add_architecture_nodes(dot, child, node_id, depth + 1)
            else:
                lines = child.get('lines', 0)
                label = f"{child_name}"
                if lines > 0:
                    label += f"\n{lines}L"

                dot.node(node_id, label=label, fillcolor=self.colors['leaf_module'],
                        shape='box', fontcolor=self.colors['text'])
                dot.edge(parent_id, node_id, arrowhead='none')

    def generate_workflow_diagram(self, output_path: Path) -> Path:
        """Generate CLEAN, PROFESSIONAL workflow diagram."""
        logger.info("Creating professional workflow diagram...")

        dot = graphviz.Digraph(
            name='Workflow',
            format=self.output_format,
            engine='neato'
        )

        dot.attr(
            bgcolor=self.colors['bg'],
            fontname='Helvetica',
            overlap='false',
            sep='1.5'
        )

        dot.attr('node',
            shape='box',
            style='filled,rounded',
            fontname='Helvetica',
            fontsize='10',
            margin='0.4,0.2',
            penwidth='2'
        )

        dot.attr('edge',
            penwidth='2',
            arrowsize='1.0'
        )

        modules = self.project_data.get('modules', {})
        if not modules:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            dot.node('empty', 'No modules', fillcolor='#FFA500')
            dot.render(filename=output_path.stem, directory=output_path.parent, cleanup=True)
            return output_path

        workflow_data = self.project_data.get('workflow_data', {})
        hierarchy = workflow_data.get('hierarchy', {})
        dependencies = workflow_data.get('dependencies', {})
        entry_points = workflow_data.get('entry_points', [])
        leaf_modules = dependencies.get('leaf_modules', [])

        processed = set()

        for parent_dir, dir_modules in sorted(hierarchy.items()):
            cluster_id = f"cluster_{parent_dir}".replace('/', '_')
            with dot.subgraph(name=cluster_id) as cluster:
                cluster.attr(
                    label=parent_dir if parent_dir != 'root' else 'Root',
                    style='rounded,filled',
                    fillcolor=self.colors['internal_dep'],
                    color=self.colors['cluster_border'],
                    fontcolor=self.colors['text'],
                    penwidth='2'
                )

                for module_path in dir_modules:
                    if module_path in processed:
                        continue
                    processed.add(module_path)

                    module_data = modules.get(module_path, {})
                    node_id = module_path.replace('/', '_')
                    module_name = Path(module_path).stem

                    is_root = module_path in entry_points
                    is_leaf = module_path in leaf_modules

                    if is_root:
                        node_color = self.colors['root_module']
                        text_color = self.colors['text_light']
                        prefix = '🚀'
                    elif is_leaf:
                        node_color = self.colors['leaf_module']
                        text_color = self.colors['text_light']
                        prefix = '🎯'
                    else:
                        node_color = self.colors['regular_module']
                        text_color = self.colors['text_light']
                        prefix = '📦'

                    classes = len(module_data.get('classes', []))
                    functions = len(module_data.get('functions', []))
                    imports = len(module_data.get('imports', []))

                    label = f"{prefix} {module_name}"
                    label += f"\n━━━━━━━━━━"
                    label += f"\n🏛️ {classes} | ⚙️ {functions}"
                    if imports > 0:
                        label += f" | 📥 {imports}"

                    cluster.node(node_id, label=label, fillcolor=node_color,
                               fontcolor=text_color, penwidth='2.5')

        if self.show_imports:
            self._add_smart_edges(dot, modules, entry_points)

        self._add_workflow_legend(dot)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        dot.render(filename=output_path.stem, directory=output_path.parent, cleanup=True)
        logger.info(f"✓ Professional workflow diagram saved")
        return output_path

    def _add_smart_edges(self, dot, modules, entry_points):
        """Add only important edges."""
        edges = set()
        for module_path, module_data in modules.items():
            node_id = module_path.replace('/', '_')
            for dep in module_data.get('dependencies', [])[:3]:
                for other in modules.keys():
                    if dep in other.replace('/', '.'):
                        other_id = other.replace('/', '_')
                        key = (node_id, other_id)
                        if key not in edges:
                            dot.edge(node_id, other_id, color=self.colors['internal_dep'],
                                   penwidth='2', arrowsize='1.2')
                            edges.add(key)
                        break

    def _add_professional_legend(self, dot):
        """Add architecture legend."""
        with dot.subgraph(name='cluster_legend') as legend:
            legend.attr(label='Legend', style='filled,rounded',
                       color=self.colors['cluster_border'], penwidth='2')
            legend.node('leg_dir', 'Directory', fillcolor=self.colors['regular_module'],
                       shape='folder', fontcolor=self.colors['text_light'])
            legend.node('leg_py', 'Python File', fillcolor=self.colors['leaf_module'],
                       fontcolor=self.colors['text'])
            legend.edge('leg_dir', 'leg_py', style='invis')

    def _add_workflow_legend(self, dot):
        """Add workflow legend."""
        with dot.subgraph(name='cluster_legend') as legend:
            legend.attr(label='Legend', style='filled,rounded', fillcolor='#F0F0F0',
                       color=self.colors['border'], penwidth='2')
            legend.node('leg_root', '🚀 Entry Point', fillcolor=self.colors['root_module'],
                       fontcolor=self.colors['text_light'], penwidth='1.5')
            legend.node('leg_leaf', '🎯 Leaf Module', fillcolor=self.colors['leaf_module'],
                       fontcolor=self.colors['text_light'], penwidth='1.5')
            legend.node('leg_regular', '📦 Regular', fillcolor=self.colors['regular_module'],
                       fontcolor=self.colors['text_light'], penwidth='1.5')
            legend.edge('leg_root', 'leg_leaf', style='invis')
            legend.edge('leg_leaf', 'leg_regular', style='invis')
