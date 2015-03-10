from django.forms import model_to_dict as stock_model_to_dict


def verbose_name_for_field(model_class, field):
    return model_class._meta.get_field_by_name(field)[0].verbose_name


def model_dict_with_related(model, related_field_name):
    result_dict = model_to_dict(model)
    result_dict[related_field_name] = [
        x.as_dict() for x in getattr(model, related_field_name).all()
    ]
    return result_dict


def dict_with_model_filefield_urls(model):
    # Possibly use request.build_absolute_uri(url) for local development.
    return {
        field_name: getattr(getattr(model, field_name),
                            "url") for field_name in
        model._meta.get_all_field_names() if (
            hasattr(model, field_name) and
            getattr(model, field_name) and
            hasattr(getattr(model, field_name), "url"))
    }


def model_to_dict(model):
    model_dict = stock_model_to_dict(model)
    model_dict.update(dict_with_model_filefield_urls(model))
    return model_dict
