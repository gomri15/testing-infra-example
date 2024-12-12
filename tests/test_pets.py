from pprint import pformat
from backend.models.pets_models import Pet
from core.dropit import DropIt
from core.dropit_logger import setup_logger


def test_create_and_update_pet(dropit: DropIt):
    """
    Test creating a new pet with the status 'available' and updating its status to 'sold'.
    """

    new_pet = Pet(
        id=12345,
        name="Fluffy",
        photoUrls=["https://example.com/photo1.jpg"],
        status="available"
    )
    created_pet = dropit.pets_api.create_pet(new_pet)

    assert created_pet.id == new_pet.id, f"Expected ID: {new_pet.id}, got: {created_pet.id}"
    assert created_pet.name == new_pet.name, f"Expected Name: {new_pet.name}, got: {created_pet.name}"
    assert created_pet.status == "available", f"Expected Status: available, got: {created_pet.status}"

    updated_pet = dropit.pets_api.update_pet_status(created_pet, "sold")

    assert updated_pet.id == created_pet.id, f"Expected ID: {created_pet.id}, got: {updated_pet.id}"
    assert updated_pet.name == created_pet.name, f"Expected Name: {created_pet.name}, got: {updated_pet.name}"
    assert updated_pet.status == "sold", f"Expected Status: sold, got: {updated_pet.status}"


def test_find_pet_by_status(dropit):
    """
    Test finding pets by status 'available', verifying the fourth pet's name is 'Puff',
    and logging the pet object to the console.
    """
    logger = setup_logger("dropit")

    available_pets = dropit.pets_api.find_pets_by_status("available")

    assert len(available_pets) >= 4, "Less than 4 pets available."
    fourth_pet = available_pets[3]
    assert fourth_pet.name == "Puff", f"Expected name 'Puff', but got '{fourth_pet.name}'"
    logger.info(f"Fourth pet: {pformat()}")


def test_validate_pets_by_status_sold(dropit):
    """
    Test finding pets by status 'sold' and validating all returned items have the expected status.
    """

    sold_pets = dropit.pets_api.find_pets_by_status("sold")

    assert all(
        pet.status == "sold" for pet in sold_pets), "Not all pets have the status 'sold'."
