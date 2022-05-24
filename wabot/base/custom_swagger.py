from drf_yasg.inspectors.view import SwaggerAutoSchema
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator


class CustomAutoSchema(SwaggerAutoSchema):

    def get_tags(self, operation_keys=None):
        tags = self.overrides.get('tags', None) or getattr(self.view, 'my_tags', [])
        if not tags:
            tags = [
             operation_keys[0]]
        return tags


class CustomSchemaGenerator(OpenAPISchemaGenerator):

    def get_paths_object(self, paths):
        return self.__get_paths_object_order_tag(paths)

    @staticmethod
    def __get_paths_object_order_tag(paths):
        try:
            new_keys = []
            for item in list(paths.keys()):
                operation = paths.get(item).operations[(-1)][(-1)]
                index_order = operation.get('tags')[(-1)].lower()
                new_keys.append({'key': item,  'index_order': index_order})

            new_order = sorted(new_keys, key=(lambda x: x['index_order']))
            return openapi.Paths({p['key']: paths[p['key']] for p in new_order})
        except Exception:
            return openapi.Paths(paths)
