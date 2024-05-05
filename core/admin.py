from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    pass
#    group_fieldsets = True   
#    class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }

@admin.register(Brand)
class BrandTranslationOptions(TranslationAdmin):
    pass

@admin.register(Color)
class ColorTranslationAdmin(TranslationAdmin):
    pass

@admin.register(Gender)
class GenderTranslationAdmin(TranslationAdmin):
    pass


@admin.register(CaseShape)
class CaseShapeTranslationAdmin(TranslationAdmin):
    pass


@admin.register(GlassFeature)
class GlassFeatureTranslationAdmin(TranslationAdmin):
    pass

@admin.register(Style)
class StyleTranslationAdmin(TranslationAdmin):
    pass


@admin.register(Mechanism)
class MechanismTranslationAdmin(TranslationAdmin):
    pass


@admin.register(StrapType)
class StrapTypeTranslationAdmin(TranslationAdmin):
    pass

