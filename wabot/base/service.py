from django.db import models, transaction


class BaseQuerySet(models.QuerySet):
    def filter_by_id(self, object_id):
        return self.filter(id=object_id)

    def exclude_id(self, object_id):
        return self.exclude(id=object_id)

    def exclude_id_list(self, id_list):
        return self.exclude(id__in=id_list)

    def order_by_id(self):
        return self.order_by('id')

    def order_by_id_desc(self):
        return self.order_by('-id')

    def flatten_to_id_list(self):
        return self.values_list('id', flat=True)


class ModelServiceMixin(object):

    model = object

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        raise

    def delete(self, *args, **kwargs):
        raise

    @classmethod
    def save_object(cls, model_object):
        with transaction.atomic():
            model_object.full_clean()
            model_object.save()
            return model_object

    @classmethod
    def get_all(cls, using_db=None):
        return cls.get_queryset_manager().all() \
            if using_db is None else cls.get_queryset_manager().using(using_db).all()

    @classmethod
    def get_none(cls, using_db=None):
        return cls.get_queryset_manager().none()

    @classmethod
    def get_object_by_id(cls, object_id, using_db=None):
        try:
            return cls.get_queryset_manager().get(id=object_id) \
                if using_db is None else cls.get_queryset_manager().using(using_db).get(id=object_id)
        except Exception:
            return None

    @classmethod
    def get_objects_in_id_list(cls, object_id_list, using_db=None):
        return cls.get_queryset_manager().filter(id__in=object_id_list) \
            if using_db is None else cls.get_queryset_manager().using(using_db).filter(id__in=object_id_list)

    @classmethod
    def _initiate_queryset_if_queryset_is_none(cls, queryset, using_db=None):
        if not queryset:
            queryset = cls.get_all(using_db=using_db)
        return queryset

    @classmethod
    def get_class_model(cls):
        return cls.model

    @classmethod
    def get_queryset_manager(cls):
        return BaseQuerySet(cls.model)
