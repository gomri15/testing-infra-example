from logging import Logger
from typing import List
from backend.models.pets_models import Pet
from playwright.sync_api import APIRequestContext


class PetsApiClient:
    def __init__(self, request_context: APIRequestContext, base_url: str, logger: Logger):
        """
        Initialize the Pets API client with Playwright's APIRequestContext.
        """
        self.request_context = request_context
        self.base_url = base_url
        self.logger = logger 

    def create_pet(self, pet: Pet) -> Pet:
        """
        Create a new pet using the Pet model.
        """
        response = self.request_context.post(
            f"{self.base_url}/pet", data=pet.model_dump())
        self.logger.info(f"Created pet: {response.json()}")
        return Pet(**response.json())

    def update_pet_status(self, pet: Pet, status: str) -> Pet:
        """
        Update the status of a pet.
        """
        pet.status = status
        response = self.request_context.put(
            f"{self.base_url}/pet", data=pet.model_dump())
        return Pet(**response.json())

    def find_pets_by_status(self, status: str) -> List[Pet]:
        """
        Find pets by their status.
        """
        response = self.request_context.get(
            f"{self.base_url}/pet/findByStatus", params={"status": status})
        return [Pet(**item) for item in response.json()]

    def validate_pets_by_status(self, status: str):
        """
        Validate that all returned pets have the expected status.
        """
        pets = self.find_pets_by_status(status)
        for pet in pets:
            assert pet.status == status, f"Pet ID {pet.id} has unexpected status: {pet.status}"
        return pets
