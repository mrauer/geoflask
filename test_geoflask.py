import geoflask


def test_sizeof_fmt_mb():
    """Test size returned is in MB."""
    assert geoflask.sizeof_fmt(121821489) == '116.2MiB'
