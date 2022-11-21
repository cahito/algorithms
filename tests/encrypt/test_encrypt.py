import pytest
from challenges.challenge_encrypt_message import encrypt_message


@pytest.fixture
def mocked_data():
    data = [
        "AABBCC",
        3,
        2,
        9,
        -1,
        "BAA_CCB",
        "CCBB_AA",
        "CCBBAA",
        "texto",
        123456,
    ]
    return data


def test_encrypt_message(mocked_data):
    (
        message,
        odd,
        even,
        out_range,
        negative,
        odd_result,
        even_result,
        out_result,
        text,
        numbers,
    ) = mocked_data
    result_1 = encrypt_message(message, odd)
    assert result_1 == odd_result
    result_2 = encrypt_message(message, even)
    assert result_2 == even_result
    result_3 = encrypt_message(message, out_range)
    assert result_3 == out_result
    result_4 = encrypt_message(message, negative)
    assert result_4 == out_result
    result_5 = encrypt_message(message, even)
    assert result_5 is not None
    with pytest.raises(TypeError):
        encrypt_message(message, text)
    with pytest.raises(TypeError):
        encrypt_message(numbers, odd)
