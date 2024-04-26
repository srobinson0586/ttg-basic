//This is the file for test functions
#include "c_programtest_1.h"
#include "unity.h"

//test names are as test_#_test   test messages start with test_#_# where
// second # == count of test_assert_* calls.


void setUp(void)
{
  /* This is run before EACH TEST */

}

void tearDown(void)
{
}

void test_1_test(void)
{
  TEST_MESSAGE("test_1_1 ASSERT_EQUAL(100, test_1(100))");
  TEST_ASSERT_EQUAL(100, test_1(100));
  TEST_MESSAGE("test_1_2 ASSERT_EQUAL(-1, test_1(65535))");
  TEST_ASSERT_EQUAL(-1, test_1(65535));
  TEST_MESSAGE("test_1_3 ASSERT_EQUAL(32767, test_1(32767))");
  TEST_ASSERT_EQUAL(32767, test_1(32767));
}

void test_2_test(void)
{
  TEST_MESSAGE("test_2_1 ASSERT_EQUAL(false, test_2(4,true))");
  TEST_ASSERT_EQUAL(false, test_2(4,true));
  TEST_MESSAGE("test_2_2 ASSERT_EQUAL(true, test_2(7,true))");
  TEST_ASSERT_EQUAL(true, test_2(7, true));
  TEST_MESSAGE("test_2_3 ASSERT_EQUAL(true, test_2(4,false))");
  TEST_ASSERT_EQUAL(true, test_2(4,false));
  TEST_MESSAGE("test_2_4 ASSERT_EQUAL(true, test_2(7,false))");
  TEST_ASSERT_EQUAL(true, test_2(7, false));

}

void test_3_test(void)
{
  TEST_MESSAGE("test_3_1 ASSERT_EQUAL(false, 'X'))");
  TEST_ASSERT_EQUAL(false, test_3('X'));
  TEST_MESSAGE("test_3_2 ASSERT_EQUAL(true, 'x'))");
  TEST_ASSERT_EQUAL(true, test_3('x'));
  TEST_MESSAGE("test_3_3 ASSERT_EQUAL(false, ']'))");
  TEST_ASSERT_EQUAL(false, test_3(']'));
  TEST_MESSAGE("test_3_4 ASSERT_EQUAL(false, '@'))");
  TEST_ASSERT_EQUAL(false, test_3('@'));
  TEST_MESSAGE("test_3_5 ASSERT_EQUAL(false, '{'))");
  TEST_ASSERT_EQUAL(false, test_3('{'));
  TEST_MESSAGE("test_3_6 ASSERT_EQUAL(true, 'C'))");
  TEST_ASSERT_EQUAL(true, test_3('C'));
  TEST_MESSAGE("test_3_7 ASSERT_EQUAL(true, 'z'))");
  TEST_ASSERT_EQUAL(true, test_3('z'));
  TEST_MESSAGE("test_3_8 ASSERT_EQUAL(true, 'Z'))");
  TEST_ASSERT_EQUAL(true, test_3('Z'));
  TEST_MESSAGE("test_3_9 ASSERT_EQUAL(true, 'a'))");
  TEST_ASSERT_EQUAL(true, test_3('a'));
  TEST_MESSAGE("test_3_10 ASSERT_EQUAL(true, 'A'))");
  TEST_ASSERT_EQUAL(true, test_3('A'));
  TEST_MESSAGE("test_3_11 ASSERT_EQUAL(true, 96))");
  TEST_ASSERT_EQUAL(false, test_3(96));
}

void test_4_test(void)
{
   TEST_MESSAGE("test_4_1 ASSERT_EQUAL(true, 13))");
  TEST_ASSERT_EQUAL(true, am_i_prime(13));
  TEST_MESSAGE("test_4_2 ASSERT_EQUAL(false, 2))");
  TEST_ASSERT_EQUAL(false, am_i_prime(2));
  TEST_MESSAGE("test_4_3 ASSERT_EQUAL(false, 999))");
  TEST_ASSERT_EQUAL(false, am_i_prime(99));
  TEST_MESSAGE("test_4_4 ASSERT_EQUAL(true, 3))");
  TEST_ASSERT_EQUAL(true, am_i_prime(3));
  TEST_MESSAGE("test_4_5 ASSERT_EQUAL(false, 1000))");
  TEST_ASSERT_EQUAL(false, am_i_prime(1000));
  TEST_MESSAGE("test_4_6 ASSERT_EQUAL(true, 953))");
  TEST_ASSERT_EQUAL(true, am_i_prime(953));
  TEST_MESSAGE("test_4_7 ASSERT_EQUAL(false, 1))");
  TEST_ASSERT_EQUAL(false, am_i_prime(1));
  TEST_MESSAGE("test_4_8 ASSERT_EQUAL(true, 47))");
  TEST_ASSERT_EQUAL(true, am_i_prime(47));
  TEST_MESSAGE("test_4_9 ASSERT_EQUAL(false, 1001))");
  TEST_ASSERT_EQUAL(false, am_i_prime(1001));
  TEST_MESSAGE("test_4_10 ASSERT_EQUAL(true, 313))");
  TEST_ASSERT_EQUAL(true, am_i_prime(313));
  TEST_MESSAGE("test_4_11 ASSERT_EQUAL(false, 93))");
  TEST_ASSERT_EQUAL(false, am_i_prime(93));
}



int main (void) 
{
UNITY_BEGIN();
RUN_TEST(test_1_test);
RUN_TEST(test_2_test);
RUN_TEST(test_3_test);
RUN_TEST(test_4_test);
return UNITY_END();
}
