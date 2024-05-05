from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('model','description',)


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('brand',)   


@register(StrapType)
class BrandTranslationOptions(TranslationOptions):
    fields = ('strap_type',)   

@register(Gender)
class GenderTranslationOptions(TranslationOptions):
    fields = ('gender',)       

@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(CaseShape)
class CaseShapeTranslationOptions(TranslationOptions):
    fields = ('case_shape',)    

@register(GlassFeature)
class GlassFeatureTranslationOptions(TranslationOptions):
    fields = ('glass_feature',)                   

@register(Style)
class StyleTranslationOptions(TranslationOptions):
    fields = ('style',)     

@register(Mechanism)
class MechanismTranslationOptions(TranslationOptions):
    fields = ('mechanism',)     