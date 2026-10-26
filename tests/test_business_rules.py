from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
    needs_second_chef,
    needs_signoff,
    total_booked,
    largest_event,
    format_event_line,
)


def test_food_cost_multiplies_price_by_guests():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_no_discount_at_24_guests():
    assert get_event_discount(24) == 0.0


def test_five_percent_discount_at_25_guests():
    assert get_event_discount(25) == 0.05


def test_five_percent_discount_at_99_guests():
    assert get_event_discount(99) == 0.05


def test_regular_event_gets_five_percent_at_100_guests():
    assert get_event_discount(100) == 0.05


def test_nonprofit_gets_twelve_percent_at_100_guests():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_nonprofit_gets_only_five_percent_at_99_guests():
    assert get_event_discount(99, nonprofit=True) == 0.05


def test_service_fee_added_at_exactly_500():
    assert round(calculate_event_total(50.00, 10), 2) == 575.00


def test_no_service_fee_just_above_500():
    assert round(calculate_event_total(50.01, 10), 2) == 500.10


def test_event_total_applies_discount_then_fee():
    assert round(calculate_event_total(16.00, 30), 2) == 531.00


def test_nonprofit_flag_changes_event_total():
    regular = calculate_event_total(30.00, 120, nonprofit=False)
    nonprofit = calculate_event_total(30.00, 120, nonprofit=True)
    assert round(regular, 2) == 3420.00
    assert round(nonprofit, 2) == 3168.00


def test_no_signoff_at_exactly_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_needed_just_above_2500():
    assert needs_signoff(2500.01) is True


def test_no_second_chef_at_80_guests():
    assert needs_second_chef(80, 100.00) is False


def test_second_chef_needed_at_81_guests():
    assert needs_second_chef(81, 100.00) is True


def test_no_second_chef_just_below_3000_total():
    assert needs_second_chef(10, 2999.99) is False


def test_second_chef_needed_at_exactly_3000_total():
    assert needs_second_chef(10, 3000.00) is True


def test_total_booked_adds_every_event_total():
    events = [
        {"client": "A", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {"client": "B", "guest_price": 20.00, "guests": 80, "nonprofit": False},
    ]
    assert round(total_booked(events), 2) == 1955.00


def test_total_booked_of_empty_list_is_zero():
    assert total_booked([]) == 0.0


def test_largest_event_returns_client_with_biggest_total():
    events = [
        {"client": "A", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {"client": "B", "guest_price": 30.00, "guests": 120, "nonprofit": False},
        {"client": "C", "guest_price": 20.00, "guests": 80, "nonprofit": False},
    ]
    assert largest_event(events) == "B"


def test_largest_event_tie_returns_first_in_list():
    events = [
        {"client": "First", "guest_price": 20.00, "guests": 10, "nonprofit": False},
        {"client": "Second", "guest_price": 20.00, "guests": 10, "nonprofit": False},
    ]
    assert largest_event(events) == "First"


def test_largest_event_of_empty_list_is_empty_string():
    assert largest_event([]) == ""


def test_format_event_line_shows_no_for_false_values():
    line = format_event_line("Finch Law", 435.0, False, False)
    assert line == "Finch Law: $435.00 | sign-off: no | second chef: no"


def test_format_event_line_shows_yes_for_true_values():
    line = format_event_line("Hilltop Gym", 3420.0, True, True)
    assert line == "Hilltop Gym: $3420.00 | sign-off: yes | second chef: yes"


def test_format_event_line_always_has_two_decimals():
    line = format_event_line("Lumen Labs", 1154.25, False, True)
    assert line == "Lumen Labs: $1154.25 | sign-off: no | second chef: yes"
