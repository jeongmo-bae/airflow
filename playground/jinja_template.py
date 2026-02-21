import logging

from jinja2 import Template

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

template = Template(
    "playground of jinja template - test value = {{val}}"
)

for val in ("**jinja_template**",123,True) :
    logger.debug(template.render(val=val))