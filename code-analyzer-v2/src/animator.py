"""
Animator Module - Enhanced Implementation
Creates detailed animated flowcharts showing actual code flow
"""

import logging
from pathlib import Path
from typing import Dict, List
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patches as mpatches

logger = logging.getLogger(__name__)


class FlowAnimator:
    """Create detailed animated flowcharts."""

    def __init__(self, project_data: Dict, fps: int = 2, duration: float = 0.5, theme: str = 'default'):
        """Initialize FlowAnimator."""
        self.project_data = project_data
        self.fps = fps
        self.duration = duration
        self.theme = theme
        self.frames = []
        self.colors = self._get_colors()

    def _get_colors(self) -> Dict:
        """Get theme colors."""
        themes = {
            'default': {'module': '#4A90E2', 'class': '#F5A623', 'function': '#BD10E0', 'flow': '#7ED321'},
            'dark': {'module': '#3498DB', 'class': '#E67E22', 'function': '#9B59B6', 'flow': '#2ECC71'},
            'colorful': {'module': '#FF6B6B', 'class': '#FFE66D', 'function': '#FF8B94', 'flow': '#A8E6CF'},
            'minimal': {'module': '#555555', 'class': '#777777', 'function': '#999999', 'flow': '#666666'}
        }
        return themes.get(self.theme, themes['default'])

    def create_animated_flowchart(self, output_path: Path) -> Path:
        """Create detailed animated flowchart."""
        logger.info("Creating detailed animated flowchart...")

        modules = self.project_data.get('modules', {})

        if not modules:
            logger.warning("No modules found, creating placeholder animation")
            return self._create_placeholder_animation(output_path)

        # Create animation showing code structure
        fig, ax = plt.subplots(figsize=(12, 8))
        fig.patch.set_facecolor('white')

        # Get modules to animate
        module_list = list(modules.items())[:15]  # Limit to 15 modules

        def animate(frame):
            ax.clear()
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            ax.axis('off')

            # Title
            ax.text(5, 9.5, 'Code Structure Flow Animation',
                   ha='center', va='center', fontsize=16, fontweight='bold')

            # Progress indicator
            progress = (frame + 1) / len(module_list)
            ax.add_patch(plt.Rectangle((1, 9), 8 * progress, 0.2,
                                      facecolor=self.colors['flow'], edgecolor='black'))
            ax.text(5, 9.1, f'Analyzing: {frame + 1}/{len(module_list)} modules',
                   ha='center', fontsize=10)

            if frame < len(module_list):
                module_path, module_data = module_list[frame]
                module_name = Path(module_path).stem

                # Module box (center)
                module_box = FancyBboxPatch((3.5, 6), 3, 1.5,
                                          boxstyle="round,pad=0.1",
                                          facecolor=self.colors['module'],
                                          edgecolor='black', linewidth=2)
                ax.add_patch(module_box)
                ax.text(5, 6.75, f'Module: {module_name}', ha='center', fontsize=12,
                       fontweight='bold', color='white')

                # Statistics
                stats_text = f"Lines: {module_data.get('lines', 0)} | "
                stats_text += f"Classes: {len(module_data.get('classes', []))} | "
                stats_text += f"Functions: {len(module_data.get('functions', []))}"
                ax.text(5, 6.3, stats_text, ha='center', fontsize=8, color='white')

                # Classes (left side)
                classes = module_data.get('classes', [])[:3]
                y_pos = 4.5
                for i, cls in enumerate(classes):
                    class_box = FancyBboxPatch((0.5, y_pos - i*0.8), 2.5, 0.6,
                                             boxstyle="round,pad=0.05",
                                             facecolor=self.colors['class'],
                                             edgecolor='black')
                    ax.add_patch(class_box)
                    ax.text(1.75, y_pos - i*0.8 + 0.3, f"Class: {cls['name']}",
                           ha='center', fontsize=9)

                    # Arrow from module to class
                    arrow = FancyArrowPatch((3.5, 6.5), (3, y_pos - i*0.8 + 0.3),
                                          arrowstyle='->', mutation_scale=15,
                                          color='gray', linestyle='dashed')
                    ax.add_patch(arrow)

                # Functions (right side)
                functions = module_data.get('functions', [])[:3]
                y_pos = 4.5
                for i, func in enumerate(functions):
                    func_box = FancyBboxPatch((7, y_pos - i*0.8), 2.5, 0.6,
                                            boxstyle="round,pad=0.05",
                                            facecolor=self.colors['function'],
                                            edgecolor='black')
                    ax.add_patch(func_box)
                    ax.text(8.25, y_pos - i*0.8 + 0.3, f"Func: {func['name']}",
                           ha='center', fontsize=9)

                    # Arrow from module to function
                    arrow = FancyArrowPatch((6.5, 6.5), (7, y_pos - i*0.8 + 0.3),
                                          arrowstyle='->', mutation_scale=15,
                                          color='gray', linestyle='dashed')
                    ax.add_patch(arrow)

                # Dependencies (bottom)
                deps = module_data.get('dependencies', [])[:3]
                if deps:
                    ax.text(5, 2, 'Dependencies:', ha='center', fontsize=10, fontweight='bold')
                    dep_text = ', '.join(deps)
                    ax.text(5, 1.5, dep_text, ha='center', fontsize=8)

            # Legend
            legend_elements = [
                mpatches.Patch(facecolor=self.colors['module'], label='Module'),
                mpatches.Patch(facecolor=self.colors['class'], label='Class'),
                mpatches.Patch(facecolor=self.colors['function'], label='Function')
            ]
            ax.legend(handles=legend_elements, loc='lower right', fontsize=8)

        # Create animation
        anim = animation.FuncAnimation(
            fig,
            animate,
            frames=len(module_list),
            interval=int(self.duration * 1000),
            repeat=True
        )

        # Save as GIF
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        writer = animation.PillowWriter(fps=self.fps)
        anim.save(output_path, writer=writer)
        plt.close()

        logger.info(f"✓ Animated flowchart saved: {output_path}")
        return output_path

    def _create_placeholder_animation(self, output_path: Path) -> Path:
        """Create placeholder animation when no modules found."""
        fig, ax = plt.subplots(figsize=(8, 6))

        def animate(frame):
            ax.clear()
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            ax.axis('off')

            x = 1 + (frame / 10) * 8
            circle = Circle((x, 5), 0.5, color='blue', alpha=0.7)
            ax.add_patch(circle)

            ax.text(5, 8, 'Code Flow Animation', ha='center', fontsize=16)
            ax.text(5, 2, f'Step {frame + 1}/10', ha='center', fontsize=12)

        anim = animation.FuncAnimation(fig, animate, frames=10,
                                     interval=int(self.duration * 1000))

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        writer = animation.PillowWriter(fps=self.fps)
        anim.save(output_path, writer=writer)
        plt.close()

        return output_path
