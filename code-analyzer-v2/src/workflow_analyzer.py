"""
Workflow Analyzer Module - IMPROVED Implementation
==================================================
Creates clean, professional workflow diagrams with proper organization
"""

import logging
from typing import Dict, List, Set, Tuple
import networkx as nx
from collections import defaultdict

logger = logging.getLogger(__name__)


class WorkflowAnalyzer:
    """Analyze code workflows and dependencies comprehensively."""

    def __init__(self, project_data: Dict):
        """Initialize WorkflowAnalyzer."""
        self.project_data = project_data
        self.workflow_graph = nx.DiGraph()
        self.module_hierarchy = {}  # For better clustering

    def analyze(self) -> Dict:
        """Perform comprehensive workflow analysis."""
        logger.info("Analyzing workflows and dependencies...")

        modules = self.project_data.get('modules', {})

        if not modules:
            logger.warning("No Python modules found for workflow analysis")
            return self._create_empty_workflow()

        # Organize modules by directory
        self._build_module_hierarchy(modules)

        # Build lightweight graph (only module level, not class/method level)
        self._build_lightweight_graph(modules)

        # Calculate metrics
        metrics = self._calculate_comprehensive_metrics()

        return {
            'graph': self.workflow_graph,
            'metrics': metrics,
            'entry_points': self._find_entry_points(),
            'modules': modules,
            'dependencies': self._analyze_dependencies(),
            'hierarchy': self.module_hierarchy
        }

    def _build_module_hierarchy(self, modules: Dict):
        """Organize modules by directory hierarchy."""
        for module_path in modules.keys():
            parts = module_path.split('/')
            if len(parts) > 1:
                parent_dir = '/'.join(parts[:-1])
            else:
                parent_dir = 'root'

            if parent_dir not in self.module_hierarchy:
                self.module_hierarchy[parent_dir] = []

            self.module_hierarchy[parent_dir].append(module_path)

    def _build_lightweight_graph(self, modules: Dict):
        """Build lightweight graph with only important connections."""
        # Add module nodes with metadata
        for module_path, module_data in modules.items():
            self.workflow_graph.add_node(
                module_path,
                type='module',
                complexity=module_data.get('complexity', 0),
                num_classes=len(module_data.get('classes', [])),
                num_functions=len(module_data.get('functions', [])),
                num_imports=len(module_data.get('imports', []))
            )

        # Add only significant dependencies (to avoid clutter)
        for module_path, module_data in modules.items():
            for dep in module_data.get('dependencies', []):
                # Check if it's an internal dependency
                for other_module in modules.keys():
                    # Check if this is an internal import
                    if (dep in other_module.replace('/', '.').replace('.py', '') or
                        other_module.replace('/', '.').replace('.py', '').endswith(dep)):

                        # Only add edge if it's meaningful
                        if self.workflow_graph.has_node(other_module):
                            self.workflow_graph.add_edge(
                                module_path,
                                other_module,
                                relationship='imports',
                                weight=1
                            )
                        break

    def _analyze_dependencies(self) -> Dict:
        """Analyze dependency structure."""
        deps = {
            'internal': defaultdict(list),
            'external': defaultdict(list),
            'root_modules': [],
            'leaf_modules': []
        }

        modules = self.project_data.get('modules', {})
        all_module_names = set(modules.keys())

        # Find root (no dependencies) and leaf (no dependents) modules
        for node in self.workflow_graph.nodes():
            if self.workflow_graph.in_degree(node) == 0:
                deps['root_modules'].append(node)
            if self.workflow_graph.out_degree(node) == 0:
                deps['leaf_modules'].append(node)

        # Categorize dependencies
        for module_path, module_data in modules.items():
            for dep in module_data.get('dependencies', []):
                if any(dep in str(m) for m in all_module_names):
                    deps['internal'][module_path].append(dep)
                else:
                    deps['external'][module_path].append(dep)

        return deps

    def _calculate_comprehensive_metrics(self) -> Dict:
        """Calculate comprehensive workflow metrics."""
        metrics = {
            'num_nodes': self.workflow_graph.number_of_nodes(),
            'num_edges': self.workflow_graph.number_of_edges(),
            'density': nx.density(self.workflow_graph) if self.workflow_graph.number_of_nodes() > 0 else 0,
            'is_dag': nx.is_directed_acyclic_graph(self.workflow_graph)
        }

        # Calculate centrality measures (only if graph has nodes)
        if metrics['num_nodes'] > 0:
            try:
                metrics['in_degree_centrality'] = nx.in_degree_centrality(self.workflow_graph)
                metrics['out_degree_centrality'] = nx.out_degree_centrality(self.workflow_graph)
            except:
                pass

        # Find most connected modules
        if metrics['num_nodes'] > 0:
            degree_dict = dict(self.workflow_graph.degree())
            metrics['most_connected'] = sorted(
                degree_dict.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]

        return metrics

    def _find_entry_points(self) -> List[str]:
        """Find potential entry points (modules with no incoming edges)."""
        entry_points = [
            node for node in self.workflow_graph.nodes()
            if self.workflow_graph.in_degree(node) == 0
        ]
        return entry_points

    def _create_empty_workflow(self) -> Dict:
        """Create empty workflow for error cases."""
        return {
            'graph': self.workflow_graph,
            'metrics': {'num_nodes': 0, 'num_edges': 0},
            'entry_points': [],
            'modules': {},
            'dependencies': {'internal': {}, 'external': {}},
            'hierarchy': {}
        }
