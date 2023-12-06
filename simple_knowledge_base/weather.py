from owlready2 import *

namespace = 'http://test.org/weather.owl'

onto = get_ontology(namespace)

with onto:
    class Weather(Thing):
        def tip(self):
            print('Hmm, not sure what your weather is..')

    class has_temperature(Weather >> int, FunctionalProperty):
        pass

    class has_humidity(Weather >> float, FunctionalProperty):
        pass

    class has_air_pressure_dropped_significantly(Weather >> bool, FunctionalProperty):
        pass

    class has_wind_speed(Weather >> int, FunctionalProperty):
        pass

    class has_precipitation(Weather >> bool, FunctionalProperty):
        pass

    class IcyAndHazardous(Weather):
        equivalent_to = [
            Weather
            & has_temperature.some(ConstrainedDatatype(int, max_inclusive=0))
            & has_precipitation.value(True)]

        def tip(self): print("It's icy and hazardous! You should use caution while driving or walking, "
                             "wear appropriate footwear, and clear any ice from "
                             "walkways and driveways.")

    class SlushyAndWet(Weather):
        equivalent_to = [
            Weather
            & has_temperature.some(ConstrainedDatatype(int, min_inclusive=0, max_inclusive=7))
            & has_precipitation.value(True)]

        def tip(self): print("It's slushy and wet! You should waterproof footwear and clothing, and use caution while "
                             "driving or walking.")

    class WindyAndDangerous(Weather):
        equivalent_to = [
            Weather
            & has_wind_speed.some(ConstrainedDatatype(int, min_inclusive=40))]

        def tip(self): print("It's windy and potentially dangerous! You should secure loose objects and avoid outdoor "
                             "activities that may be hazardous in strong winds.")

    class HotAndHumid(Weather):
        equivalent_to = [
            Weather
            & has_temperature.some(ConstrainedDatatype(int, min_inclusive=27))
            & has_humidity.some(ConstrainedDatatype(float, min_inclusive=0.6))]

        def tip(self): print("It's hot and humid! You should wear light and breathable clothing, stay hydrated, "
                             "and avoid prolonged outdoor activities during the hottest part of the day.")

    class Stormy(Weather):
        equivalent_to = [
            Weather
            & has_air_pressure_dropped_significantly.exactly(True)]

        def tip(self): print("Storm or weather front approaching! You should monitor local weather reports and be "
                             "prepared for changes in the weather, such as thunderstorms or heavy rain.")


print('Before:')
weather1 = Weather('weather1')
print(weather1.name)
weather1.tip()

weather1.has_temperature = -1
weather1.has_precipitation = True

print()

weather2 = Weather('weather2')
print(weather2.name)
weather2.tip()

weather2.has_temperature = 5
weather2.has_precipitation = True

print()

weather3 = Weather('weather3')
print(weather3.name)
weather3.tip()

weather3.has_wind_speed = 50

print()

weather4 = Weather('weather4')
print(weather4.name)
weather4.tip()

weather4.has_temperature = 30
weather4.has_humidity = 0.7

print()

weather5 = Weather('weather5')
print(weather5.name)
weather5.tip()

weather5.has_air_pressure_dropped_significantly = True

print()
sync_reasoner()

print('After:')

print(weather1.name)
weather1.tip()

print()

print(weather2.name)
weather2.tip()

print()

print(weather3.name)
weather3.tip()

print()

print(weather4.name)
weather4.tip()

print()

print(weather5.name)
weather5.tip()

onto.save(file='weather.owl', format="rdfxml")