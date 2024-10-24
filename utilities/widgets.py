from django.forms import widgets
from django.utils.safestring import mark_safe
import json

class QuillEditorWidget(widgets.Textarea):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        attrs['style'] = 'display:none;'
        text_area = super().render(name, value, attrs, renderer)
        quill_html = f'''
            <div class="custom-quill-container">
                <div id="{name}_quill" class="custom-quill" style="height: 300px;"></div>
            </div>
            <script>
                document.addEventListener("DOMContentLoaded", function() {{
                    var quill = new Quill("#{name}_quill", {json.dumps(self.options)});
                    var textarea = document.querySelector("textarea[name='{name}']");
                    quill.on('text-change', function() {{
                        textarea.value = quill.root.innerHTML;
                    }});
                    quill.root.innerHTML = {json.dumps(value)};
                }});
            </script>
        '''
        return mark_safe(text_area + quill_html)
