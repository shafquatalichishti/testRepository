import unittest
import functions


class functions_Test(unittest.TestCase):

    def test_Validint(number):
        actual_result = functions.isAInt(5)
        expected_result = True

        number.assertEqual(expected_result, actual_result)

    def test_Invalidint(number):
        actual_result = functions.isAInt('a')
        expected_result = False

        number.assertEqual(expected_result, actual_result)


    def test_ValidChoice(choice):
        actual_result = functions.isValidChoice('5')
        expected_result = True

        choice.assertEqual(expected_result, actual_result)

    def test_inValidChoice(choice):
        actual_result = functions.isValidChoice('8')
        expected_result = False
        # 8 isn't in the choice range
        choice.assertEqual(expected_result, actual_result)

    def test_ValidName(name):
        actual_result = functions.isValidName('Jason')
        expected_result = True

        name.assertEqual(expected_result, actual_result)

    def test_inValidName(name):
        actual_result = functions.isValidName('JasonAmyCindySooNatarapimoetestdata')
        expected_result = False
        #It's more than 30 characters, so should be false
        name.assertEqual(expected_result, actual_result)

    def test_ValidPosition(position):
        actual_result = functions.isValidPosition('Forward')
        expected_result = True

        position.assertEqual(expected_result, actual_result)

    def test_inValidPosition(position):
        actual_result = functions.isValidPosition('Forwarding')
        expected_result = False

        position.assertEqual(expected_result, actual_result)

    def test_ValidInputNumber(number):
        actual_result = functions.isValidInputNumber('5',1,8)
        expected_result = True

        number.assertEqual(expected_result, actual_result)

    def test_inValidInputNumber(number):
        actual_result = functions.isValidInputNumber('9', 1, 8)
        expected_result = False

        number.assertEqual(expected_result, actual_result)

    def test_ValidInputNumber2(number):
        actual_result = functions.isValidInputNumber('1', 1, 8)
        expected_result = True

        number.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()