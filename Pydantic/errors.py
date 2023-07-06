# Pydantic is a powerful parsing library that validates input data during runtime. 

from pydantic import BaseModel
import functools

class Car(BaseModel):  
    brand: str
    cubic_centimetres: int
    name: str 

    @functools.cached_property
    def hp(self) -> float:
        return self.cc / 15

    class Config:  
        allow_population_by_field_name = True  
        fields = {"cubic_centimetres": {"alias": "cc"}} 

        validate_assignment =True

        keep_untouched = (functools.cached_property,)

        extra = "allow"

  
  

Car.Config.allow_population_by_field_name = False  
Car(brand="Ford", cubic_centimetres=1500, name="Kuga")  # Failed
#> Traceback (most recent call last):
#> ...
#> pydantic.error_wrappers.ValidationError: 1 validation error for Car
#> cc
#>   field required (type=value_error.missing)


car = Car(brand="Ford", cc=1500, name="Kuga", extra_arg=5)  ## extra = 'ignore'
print(car.extra_arg)  # Failed
#> Traceback (most recent call last):
#> ...
#> AttributeError: 'Car' object has no attribute 'extra_arg'



car = Car(brand="Ford", cc=1500, name="Kuga", extra_arg=5)  ## extra = 'forbid'
#> Traceback (most recent call last):
#> ...
#> pydantic.error_wrappers.ValidationError: 1 validation error for Car
#> extra_arg
#>  extra fields not permitted (type=value_error.extra)


car = Car(brand="Ford", cc=1500, name="Kuga") # without `keep_untouched`
#> Traceback (most recent call last):
#> ...
#> TypeError: cannot pickle '_thread.RLock' object


car = Car(brand="Ford", cc=1500, name="Kuga", extra_arg=5)  ## extra = 'forbid'
#> Traceback (most recent call last):
#> ...
#> pydantic.error_wrappers.ValidationError: 1 validation error for Car
#> extra_arg
#>  extra fields not permitted (type=value_error.extra)