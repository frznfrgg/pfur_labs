class Temperature:
    """Simple temperature class"""

    def __init__(self, celsius: float):
        """Initializes temperature class

        Args:
            celsius (float): temperature level in celsius
        """
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Returns temperature level in celsius

        Returns:
            float: temp level
        """
        return self._celsius

    @celsius.setter
    def celsius(self, temp_c: float):
        """Sets temperature in celcius

        Args:
            temp_c (float): temp value

        Raises:
            ValueError: raised if temp is not a number
        """
        if not isinstance(temp_c, (int, float)):
            raise ValueError("Temp must be either int or fload")
        self._celsius = temp_c

    @property
    def fahrenheit(self) -> float:
        """Temperature in fahrenheit degrees

        Returns:
            float: temp in fahrenheit
        """
        return self._celsius * 9 / 5 + 32
