from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
    needs_second_chef,
    needs_signoff,
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
