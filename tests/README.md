# SlotManager Unit Tests

This directory contains unit tests for the `SlotManager` class from the autoreg-for-homies system.

## Test Structure

The test suite is organized into two main test classes:

### TestSlotManager
Basic unit tests for individual `SlotManager` methods and functionality:

- **test_initialization**: Tests proper initialization of SlotManager instances
- **test_property_getters**: Tests all property getter methods
- **test_property_setters**: Tests all property setter methods
- **test_is_in_any_list**: Tests player existence checking across all lists
- **test_register_new_player**: Tests registering new players
- **test_register_when_full**: Tests registration when main list is full
- **test_register_duplicate_player**: Tests duplicate player handling
- **test_register_from_non_pending_reservations**: Tests moving players from reservations
- **test_reserve_player**: Tests basic player reservation
- **test_reserve_pending_player**: Tests reserving players from pending list
- **test_restructure**: Tests the restructure functionality
- **test_get_num_available**: Tests available slot counting
- **test_to_string**: Tests string representation formatting
- **test_private_methods**: Placeholder for testing private methods
- **test_edge_cases**: Tests boundary conditions and edge cases

### TestSlotManagerIntegration
Integration tests for complex workflows:

- **test_complete_workflow**: Tests complete registration/reservation workflow
- **test_multiple_reserves_and_registrations**: Tests complex multi-operation scenarios

## Running the Tests

### Method 1: Using the test runner script
```bash
chmod +x run_tests.sh
./run_tests.sh
```

### Method 2: Using Python unittest directly
```bash
cd /workspaces/autoreg-for-homies
python -m unittest tests.test_slot_manager -v
```

### Method 3: Running specific test methods
```bash
python -m unittest tests.test_slot_manager.TestSlotManager.test_initialization -v
```

## Test Implementation Status

This test suite contains **placeholder test cases** with TODO comments indicating areas for implementation. Each test method includes:

1. Basic structural setup
2. TODO comments describing what should be implemented
3. Some basic assertions to demonstrate expected functionality

## Key Features Tested

- **Player Registration**: Adding players to main list or pending reservations
- **Player Reservation**: Moving players to non-pending reservations  
- **List Management**: Proper handling of players, pending, and non-pending lists
- **Restructuring**: Automatic promotion of pending players to main list
- **Validation**: Name conflict detection and edge case handling
- **String Formatting**: Proper display of slot information

## Dependencies

The tests require:
- Python 3.x
- Access to the `auto_registration_system` package
- `unittest` module (standard library)

## Notes

- All test methods include placeholder implementations with TODO comments
- The tests use proper setUp/tearDown methods for clean test isolation
- Integration tests demonstrate real-world usage patterns
- Error handling tests verify proper exception raising