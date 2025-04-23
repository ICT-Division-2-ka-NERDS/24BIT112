class Weather:
    def __init__(self, parameters):
        self.parameters = parameters
    def __contains__(self, item):
        return item in self.parameters

w = Weather(['rainy', 'sunny', 'windy'])
print('rainy' in w)
print('cloudy' in w)