# Author: Mayank Kumar Pokhriyal
# Date: 21st Feb 2025
# Description: Test file for checking errors in pyramid Area.
import pytest
import pyramidArea as pa

def test_calcBaseArea():
    """Test valid base area calculation"""
    assert pa.calcBaseArea(15) == 225

@pytest.mark.xfail(reason="Input should not be text!")
def test_calcBaseAreaText():
    pa.calcBaseArea("5")

def test_calcSideAreaBetween():
    """Test side area calculation within range"""
    result = pa.calcSideArea(15, 5)
    assert 270.41 < result < 270.42

def test_calcSideAreaRound():
    """Test rounded side area calculation"""
    result = pa.calcSideArea(10, 3)
    assert round(result, 2) == 116.62

@pytest.mark.skip(reason="Only prints text to the screen.")
def test_prntSurfArea():
    """Test print function (skipped)"""
    base = pa.calcBaseArea(15)
    side = pa.calcSideArea(15, 10)
    pa.printSurfArea(base, side)