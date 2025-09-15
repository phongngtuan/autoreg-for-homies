import unittest
import sys
import os

# Add the parent directory to Python path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from auto_registration_system.data_structure.slot_manager import SlotManager
from auto_registration_system.exception.exception_name_conflict import (
    NameConflictException
)


class TestSlotManager(unittest.TestCase):
    """Unit tests for SlotManager class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.slot_manager = SlotManager("Test Slot", 3)

    def tearDown(self):
        """Clean up after each test method."""
        pass

    def test_initialization(self):
        """Test SlotManager initialization."""
        # TODO: Implement test for SlotManager initialization
        self.assertEqual(self.slot_manager.slot_name, "Test Slot")
        self.assertEqual(self.slot_manager.num_players, 3)
        self.assertEqual(len(self.slot_manager.players), 0)
        self.assertEqual(len(self.slot_manager.pending_reservations), 0)
        self.assertEqual(len(self.slot_manager.non_pending_reservations), 0)

    def test_property_getters(self):
        """Test property getters for slot_name and num_players."""
        # TODO: Implement comprehensive property getter tests
        self.assertEqual(self.slot_manager.slot_name, "Test Slot")
        self.assertEqual(self.slot_manager.num_players, 3)
        self.assertIsInstance(self.slot_manager.players, list)
        self.assertIsInstance(self.slot_manager.pending_reservations, list)
        self.assertIsInstance(self.slot_manager.non_pending_reservations, list)

    def test_property_setters(self):
        """Test property setters for lists."""
        # TODO: Implement comprehensive property setter tests
        new_players = ["Player1", "Player2"]
        new_pending = ["PendingPlayer"]
        new_non_pending = ["NonPendingPlayer"]

        self.slot_manager.players = new_players
        self.slot_manager.pending_reservations = new_pending
        self.slot_manager.non_pending_reservations = new_non_pending

        self.assertEqual(self.slot_manager.players, new_players)
        self.assertEqual(self.slot_manager.pending_reservations, new_pending)
        self.assertEqual(
            self.slot_manager.non_pending_reservations, new_non_pending
        )

    def test_is_in_any_list(self):
        """Test is_in_any_list method."""
        # Test when player is not in any list
        self.assertFalse(self.slot_manager.is_in_any_list("NonExistentPlayer"))

        # Test when player is in main players list
        self.slot_manager.players = ["Player1"]
        self.assertTrue(self.slot_manager.is_in_any_list("Player1"))

        # Test when player is in pending reservations
        self.slot_manager.pending_reservations = ["PendingPlayer"]
        self.assertTrue(self.slot_manager.is_in_any_list("PendingPlayer"))

        # Test when player is in non-pending reservations
        self.slot_manager.non_pending_reservations = ["NonPendingPlayer"]
        self.assertTrue(self.slot_manager.is_in_any_list("NonPendingPlayer"))

    def test_register_new_player(self):
        """Test registering a new player."""
        # Test registering to main list when space available
        self.slot_manager.register("Player1")
        self.assertIn("Player1", self.slot_manager.players)
        self.assertEqual(len(self.slot_manager.players), 1)

    def test_register_when_full(self):
        """Test registering when main list is full."""
        # Fill up main list
        self.slot_manager.register("Player1")
        self.slot_manager.register("Player2")
        self.slot_manager.register("Player3")

        # Register another player (should go to pending)
        self.slot_manager.register("Player4")
        self.assertIn("Player4", self.slot_manager.pending_reservations)

    def test_register_duplicate_player(self):
        """Test registering a duplicate player raises exception."""
        self.slot_manager.register("Player1")

        with self.assertRaises(NameConflictException):
            self.slot_manager.register("Player1")

    def test_register_from_non_pending_reservations(self):
        """Test registering a player from non-pending reservations."""
        # TODO: Implement test for moving player from non-pending reservations
        self.slot_manager.non_pending_reservations = ["ReservedPlayer"]
        self.slot_manager.register("ReservedPlayer")
        
        self.assertIn("ReservedPlayer", self.slot_manager.players)
        self.assertNotIn(
            "ReservedPlayer", self.slot_manager.non_pending_reservations
        )

    def test_reserve_player(self):
        """Test reserving a player."""
        self.slot_manager.register("Player1")
        # Reserving after registering moves player from main to non-pending
        self.slot_manager.reserve("Player1")
        self.assertNotIn("Player1", self.slot_manager.players)
        self.assertIn("Player1", self.slot_manager.non_pending_reservations)

    def test_reserve_pending_player(self):
        """Test reserving a player from pending list."""
        # Fill main list and add pending player
        self.slot_manager.register("Player1")
        self.slot_manager.register("Player2")
        self.slot_manager.register("Player3")
        self.slot_manager.register("Player4")  # This goes to pending
        self.slot_manager.reserve("Player4")
        self.assertNotIn(
            "Player4", self.slot_manager.pending_reservations
        )
        self.assertIn("Player4", self.slot_manager.non_pending_reservations)

    def test_restructure(self):
        """Test restructure method."""
        # Set up scenario where restructure should move pending to main
        self.slot_manager.players = ["Player1", "Player2"]
        self.slot_manager.pending_reservations = ["PendingPlayer"]
        self.slot_manager.restructure()
        self.assertIn("PendingPlayer", self.slot_manager.players)
        self.assertNotIn(
            "PendingPlayer", self.slot_manager.pending_reservations
        )
        self.assertEqual(len(self.slot_manager.players), 3)

    def test_get_num_available(self):
        """Test get_num_available method."""
        # Test when no players registered
        self.assertEqual(self.slot_manager.get_num_available(), 3)

        # Test with some players registered
        self.slot_manager.register("Player1")
        self.assertEqual(self.slot_manager.get_num_available(), 2)

        # Test when full
        self.slot_manager.register("Player2")
        self.slot_manager.register("Player3")
        self.assertEqual(self.slot_manager.get_num_available(), 0)

    def test_to_string(self):
        """Test to_string method."""
        # Test empty slot
        result = self.slot_manager.to_string("A")
        self.assertIn("[A] Test Slot", result)
        self.assertIn("#players: 3", result)

        # Test with players
        self.slot_manager.register("Player1")
        result = self.slot_manager.to_string("B")
        self.assertIn("Player1", result)

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # TODO: Implement tests for edge cases
        # Test with zero capacity slot
        zero_slot = SlotManager("Zero Slot", 0)
        self.assertEqual(zero_slot.get_num_available(), 0)
        # Test with empty strings
        empty_name_slot = SlotManager("", 1)
        self.assertEqual(empty_name_slot.slot_name, "")


class TestSlotManagerIntegration(unittest.TestCase):
    """Integration tests for SlotManager with multiple operations."""

    def setUp(self):
        """Set up test fixtures for integration tests."""
        self.slot_manager = SlotManager("Integration Test Slot", 2)

    def test_complete_workflow(self):
        """Test complete workflow of registration, reservation, etc."""
        # Register players until full
        self.slot_manager.register("Player1")
        self.slot_manager.register("Player2")
        self.slot_manager.register("Player3")  # Should go to pending

        # Reserve a main player
        self.slot_manager.reserve("Player1")

        # Verify restructuring happened
        self.assertIn("Player3", self.slot_manager.players)
        self.assertIn("Player1", self.slot_manager.non_pending_reservations)
        self.assertEqual(len(self.slot_manager.pending_reservations), 0)


if __name__ == '__main__':
    unittest.main()
