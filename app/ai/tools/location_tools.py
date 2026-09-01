class LocationTools:

    async def nearby(
        self,
        latitude: float,
        longitude: float,
        radius_km: float = 10,
    ):
        """
        Placeholder for MongoDB $geoNear implementation.
        """

        return {
            "latitude": latitude,
            "longitude": longitude,
            "radius_km": radius_km,
            "results": [],
        }