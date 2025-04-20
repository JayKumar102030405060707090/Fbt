from plugins.filters import apply_filters

async def transform_message(text, filters):
    return apply_filters(text, filters)