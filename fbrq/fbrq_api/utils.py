from rest_framework.exceptions import ValidationError


def serialize(serializer, field_name, data=None, instance=None, request=None):
    data_serializer = serializer(instance, data=data)
    if not data_serializer.is_valid(raise_exception=True):
        raise ValidationError(f'Invalid {field_name} fields')
    if request:
        return data_serializer.save(request=request)
    else:
        return data_serializer.save()


def serialize_list(
        model, serializer, field_name, data, **kwargs) -> None:
    for item_data in data:
        instance = model(**kwargs)
        print(instance)
        serialize(serializer, field_name, data=item_data, instance=instance)