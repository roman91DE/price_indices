from traitlets.config import get_config
from nbconvert.preprocessors import TagRemovePreprocessor
from nbconvert.exporters import ScriptExporter

c = get_config()

# Disable cell numbering
c.TemplateExporter.exclude_input_prompt = True
c.TemplateExporter.exclude_output_prompt = True

# Remove Testing and Visualization Cells
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags = ("remove-cell",)
c.NbConvertApp.exporter_class = "nbconvert.exporters.ScriptExporter"
c.NbConvertApp.notebook_metadata_filter = {
    "exclude": ["widgets"]
}
