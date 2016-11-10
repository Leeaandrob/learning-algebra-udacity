# coding: utf-8
from unittest import TestCase

from algebralinear.vector import Vector


class VectorTestCase(TestCase):
    def setUp(self):
        self.v1 = Vector([1.671, -1.012, -0.318])
        self.v2 = Vector([2, 4])

    def test_sum_vector(self):
        response = self.v1 + self.v2
        self.assertEqual(response, Vector([3.671, 2.988]))

    def test_sub_vector(self):
        response = self.v1 - self.v2

        self.assertEqual(response, Vector([-0.329, -5.012]))

    def test_multi_vector(self):
        response = self.v1 * 7.41
        self.assertEqual(response, Vector([12.382, -7.499, -2.356]))

    def test_magnitude_vector(self):
        v1 = Vector([-0.221, 7.437])

        self.assertEqual(v1.__mag__(), 7.44)

    def test_magnitude_vector_other_quest(self):
        v1 = Vector([8.813, -1.331, -6.247])

        self.assertEqual(v1.__mag__(), 10.884)

    def test_normalization_vector(self):
        v1 = Vector([1.996, 3.108, -4.554])

        self.assertEqual(v1.__normalize__(), Vector([0.34, 0.53, -0.777]))

    def test_normalization_other_quest(self):
        v1 = Vector([5.581, -2.136])

        self.assertEqual(v1.__normalize__(), Vector([0.934, -0.357]))
