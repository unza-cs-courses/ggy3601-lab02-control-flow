"""
Lab 2 Visible Tests - Control Flow & Functions
These tests verify core functionality of control structures and functions.
"""

import subprocess
import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent.parent.parent / "src"


def run_script(script_name, input_data=None):
    """Run a Python script and capture output."""
    script_path = SRC_DIR / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        input=input_data,
        timeout=10
    )
    return result


# ============================================================================
# Task 1: Grade Classification Tests
# ============================================================================

class TestTask1ClassifyGrade:
    """Tests for Task 1: classify_grade function"""

    def test_classify_file_exists(self):
        """lab2_classify.py file should exist"""
        assert (SRC_DIR / "lab2_classify.py").exists(), "lab2_classify.py not found in src/"

    def test_classify_runs_without_error(self):
        """lab2_classify.py should run without errors"""
        result = run_script("lab2_classify.py")
        assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    def test_classify_function_exists(self):
        """classify_grade function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_classify import classify_grade
            assert callable(classify_grade), "classify_grade should be a function"
        finally:
            sys.path.pop(0)

    def test_classify_high_grade(self, grade_thresholds):
        """Should classify high grades correctly"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_classify import classify_grade
            high_threshold = grade_thresholds['high']
            result = classify_grade(high_threshold + 0.5)
            assert result is not None, "classify_grade should return a value"
            assert "high" in result.lower(), f"Grade {high_threshold + 0.5} should be classified as High Grade"
        finally:
            sys.path.pop(0)

    def test_classify_medium_grade(self, grade_thresholds):
        """Should classify medium grades correctly"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_classify import classify_grade
            # Grade between medium and high thresholds
            test_grade = (grade_thresholds['medium'] + grade_thresholds['high']) / 2
            result = classify_grade(test_grade)
            assert result is not None, "classify_grade should return a value"
            assert "medium" in result.lower(), f"Grade {test_grade} should be Medium Grade"
        finally:
            sys.path.pop(0)

    def test_classify_low_grade(self, grade_thresholds):
        """Should classify low grades correctly"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_classify import classify_grade
            # Grade between low and medium thresholds
            test_grade = (grade_thresholds['low'] + grade_thresholds['medium']) / 2
            result = classify_grade(test_grade)
            assert result is not None, "classify_grade should return a value"
            assert "low" in result.lower(), f"Grade {test_grade} should be Low Grade"
        finally:
            sys.path.pop(0)

    def test_classify_subeconomic(self, grade_thresholds):
        """Should classify sub-economic grades correctly"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_classify import classify_grade
            # Grade between 0 and low threshold
            test_grade = grade_thresholds['low'] / 2
            result = classify_grade(test_grade)
            assert result is not None, "classify_grade should return a value"
            assert "sub" in result.lower() or "economic" in result.lower(), \
                f"Grade {test_grade} should be Sub-economic"
        finally:
            sys.path.pop(0)

    def test_classify_invalid_negative(self):
        """Should classify negative grades as Invalid"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_classify import classify_grade
            result = classify_grade(-1.0)
            assert result is not None, "classify_grade should return a value"
            assert "invalid" in result.lower(), "Negative grade should be Invalid"
        finally:
            sys.path.pop(0)

    def test_classify_zero_grade(self, grade_thresholds):
        """Should handle zero grade (valid, sub-economic)"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_classify import classify_grade
            result = classify_grade(0)
            assert result is not None, "classify_grade should return a value"
            # Zero is valid but sub-economic (not "Invalid")
            assert "invalid" not in result.lower(), "Zero grade should not be Invalid"
        finally:
            sys.path.pop(0)


# ============================================================================
# Task 2: Sample Processing Tests
# ============================================================================

class TestTask2Processing:
    """Tests for Task 2: Sample processing with for loops"""

    def test_processing_file_exists(self):
        """lab2_processing.py file should exist"""
        assert (SRC_DIR / "lab2_processing.py").exists(), "lab2_processing.py not found in src/"

    def test_processing_runs_without_error(self):
        """lab2_processing.py should run without errors"""
        result = run_script("lab2_processing.py")
        assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    def test_process_samples_function_exists(self):
        """process_samples function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_processing import process_samples
            assert callable(process_samples), "process_samples should be a function"
        finally:
            sys.path.pop(0)

    def test_process_samples_returns_dict(self, test_samples):
        """process_samples should return a dictionary"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_processing import process_samples
            result = process_samples(test_samples)
            assert result is not None, "process_samples should return a value"
            assert isinstance(result, dict), "process_samples should return a dict"
        finally:
            sys.path.pop(0)

    def test_process_samples_has_required_keys(self, test_samples):
        """process_samples should return dict with required keys"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_processing import process_samples
            result = process_samples(test_samples)
            required_keys = ['count', 'total', 'average', 'max_grade', 'min_grade']
            for key in required_keys:
                assert key in result, f"Result should contain '{key}'"
        finally:
            sys.path.pop(0)

    def test_process_samples_skips_negative(self):
        """process_samples should skip negative values"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_processing import process_samples
            samples = [1.0, -1.0, 2.0, -2.0, 3.0]
            result = process_samples(samples)
            # Should count only 3 valid samples (1.0, 2.0, 3.0)
            assert result['count'] == 3, "Should only count non-negative samples"
        finally:
            sys.path.pop(0)

    def test_count_by_category_function_exists(self):
        """count_by_category function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_processing import count_by_category
            assert callable(count_by_category), "count_by_category should be a function"
        finally:
            sys.path.pop(0)

    def test_count_by_category_returns_dict(self, test_samples, grade_thresholds):
        """count_by_category should return a dictionary"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_processing import count_by_category
            result = count_by_category(test_samples, grade_thresholds)
            assert result is not None, "count_by_category should return a value"
            assert isinstance(result, dict), "count_by_category should return a dict"
        finally:
            sys.path.pop(0)


# ============================================================================
# Task 3: Input Validation Tests
# ============================================================================

class TestTask3Validation:
    """Tests for Task 3: Input validation with while loops"""

    def test_validation_file_exists(self):
        """lab2_validation.py file should exist"""
        assert (SRC_DIR / "lab2_validation.py").exists(), "lab2_validation.py not found in src/"

    def test_get_valid_grade_function_exists(self):
        """get_valid_grade function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_validation import get_valid_grade
            assert callable(get_valid_grade), "get_valid_grade should be a function"
        finally:
            sys.path.pop(0)

    def test_get_valid_depth_function_exists(self):
        """get_valid_depth function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_validation import get_valid_depth
            assert callable(get_valid_depth), "get_valid_depth should be a function"
        finally:
            sys.path.pop(0)

    def test_collect_samples_function_exists(self):
        """collect_samples function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_validation import collect_samples
            assert callable(collect_samples), "collect_samples should be a function"
        finally:
            sys.path.pop(0)


# ============================================================================
# Task 4: Drilling Cost Calculator Tests
# ============================================================================

class TestTask4Calculator:
    """Tests for Task 4: Drilling cost calculator"""

    def test_calculator_file_exists(self):
        """lab2_calculator.py file should exist"""
        assert (SRC_DIR / "lab2_calculator.py").exists(), "lab2_calculator.py not found in src/"

    def test_calculator_runs_without_error(self):
        """lab2_calculator.py should run without errors"""
        result = run_script("lab2_calculator.py")
        assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    def test_calculate_drilling_cost_exists(self):
        """calculate_drilling_cost function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            assert callable(calculate_drilling_cost), "calculate_drilling_cost should be a function"
        finally:
            sys.path.pop(0)

    def test_calculator_tier1_only(self, base_rate):
        """Should calculate correctly for tier 1 only (0-200m)"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            # 100 meters at base rate, medium hardness (no adjustment)
            cost = calculate_drilling_cost(100, base_rate, 'medium')
            expected = 100 * base_rate
            assert cost is not None, "Function should return a value"
            assert abs(cost - expected) < 0.01, f"Expected {expected}, got {cost}"
        finally:
            sys.path.pop(0)

    def test_calculator_tier2(self, base_rate):
        """Should apply 25% surcharge for 200-500m"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            # 300 meters: 200 at base, 100 at 1.25x
            cost = calculate_drilling_cost(300, base_rate, 'medium')
            expected = (200 * base_rate) + (100 * base_rate * 1.25)
            assert cost is not None, "Function should return a value"
            assert abs(cost - expected) < 0.01, f"Expected {expected}, got {cost}"
        finally:
            sys.path.pop(0)

    def test_calculator_tier3(self, base_rate):
        """Should apply 50% surcharge for over 500m"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            # 600 meters: 200 at base, 300 at 1.25x, 100 at 1.5x
            cost = calculate_drilling_cost(600, base_rate, 'medium')
            expected = (200 * base_rate) + (300 * base_rate * 1.25) + (100 * base_rate * 1.5)
            assert cost is not None, "Function should return a value"
            assert abs(cost - expected) < 0.01, f"Expected {expected}, got {cost}"
        finally:
            sys.path.pop(0)

    def test_calculator_soft_discount(self, base_rate):
        """Should apply 10% discount for soft rock"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            cost_medium = calculate_drilling_cost(100, base_rate, 'medium')
            cost_soft = calculate_drilling_cost(100, base_rate, 'soft')
            expected_soft = cost_medium * 0.9
            assert cost_soft is not None, "Function should return a value"
            assert abs(cost_soft - expected_soft) < 0.01, \
                f"Soft rock should have 10% discount. Expected {expected_soft}, got {cost_soft}"
        finally:
            sys.path.pop(0)

    def test_calculator_hard_surcharge(self, base_rate):
        """Should apply 20% surcharge for hard rock"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            cost_medium = calculate_drilling_cost(100, base_rate, 'medium')
            cost_hard = calculate_drilling_cost(100, base_rate, 'hard')
            expected_hard = cost_medium * 1.2
            assert cost_hard is not None, "Function should return a value"
            assert abs(cost_hard - expected_hard) < 0.01, \
                f"Hard rock should have 20% surcharge. Expected {expected_hard}, got {cost_hard}"
        finally:
            sys.path.pop(0)

    def test_calculator_invalid_depth_negative(self, base_rate):
        """Should return -1 for negative depth"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            cost = calculate_drilling_cost(-100, base_rate, 'medium')
            assert cost == -1, "Negative depth should return -1"
        finally:
            sys.path.pop(0)

    def test_calculator_invalid_depth_zero(self, base_rate):
        """Should return -1 for zero depth"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            cost = calculate_drilling_cost(0, base_rate, 'medium')
            assert cost == -1, "Zero depth should return -1"
        finally:
            sys.path.pop(0)

    def test_calculator_invalid_hardness(self, base_rate):
        """Should return -1 for invalid hardness"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_calculator import calculate_drilling_cost
            cost = calculate_drilling_cost(100, base_rate, 'very_hard')
            assert cost == -1, "Invalid hardness should return -1"
        finally:
            sys.path.pop(0)


# ============================================================================
# Task 5: Statistics Report Tests
# ============================================================================

class TestTask5Statistics:
    """Tests for Task 5: Grade statistics report"""

    def test_statistics_file_exists(self):
        """lab2_statistics.py file should exist"""
        assert (SRC_DIR / "lab2_statistics.py").exists(), "lab2_statistics.py not found in src/"

    def test_statistics_runs_without_error(self):
        """lab2_statistics.py should run without errors"""
        result = run_script("lab2_statistics.py")
        assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    def test_generate_report_function_exists(self):
        """generate_report function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_statistics import generate_report
            assert callable(generate_report), "generate_report should be a function"
        finally:
            sys.path.pop(0)

    def test_find_anomalies_function_exists(self):
        """find_anomalies function should be defined"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_statistics import find_anomalies
            assert callable(find_anomalies), "find_anomalies should be a function"
        finally:
            sys.path.pop(0)

    def test_find_anomalies_returns_list(self, test_samples):
        """find_anomalies should return a list"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_statistics import find_anomalies
            result = find_anomalies(test_samples)
            if result is not None:  # Only test if implemented
                assert isinstance(result, list), "find_anomalies should return a list"
        finally:
            sys.path.pop(0)

    def test_find_anomalies_detects_outliers(self):
        """find_anomalies should detect obvious outliers"""
        sys.path.insert(0, str(SRC_DIR))
        try:
            from lab2_statistics import find_anomalies
            # Samples with one obvious outlier
            samples = [1.0, 1.5, 1.2, 1.3, 1.4, 10.0]  # 10.0 is clearly an outlier
            result = find_anomalies(samples, threshold_multiplier=2.0)
            if result is not None:  # Only test if implemented
                assert 10.0 in result, "Should detect 10.0 as an anomaly"
        finally:
            sys.path.pop(0)
