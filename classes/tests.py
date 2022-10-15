import unittest

from PriorityQueue import PriorityQueue


class PriorityQueueTests(unittest.TestCase):

    def test_add_item(self):
        queue = PriorityQueue()
        self.assertEqual(len(queue), 0)

        added_item = queue.add_item('foo', 1)
        self.assertListEqual(list(queue), ['foo'])
        self.assertEqual(added_item, 'foo')

        queue.add_item('bar', 2)
        self.assertListEqual(list(queue), ['bar', 'foo'])

        queue.add_item(42, 0)
        self.assertListEqual(list(queue), ['bar', 'foo', 42])
    
    def test_is_empty(self):
        queue = PriorityQueue()
        self.assertTrue(queue.is_empty())

        queue.add_item('foo', 1)
        self.assertFalse(queue.is_empty())

        queue.pop()
        self.assertTrue(queue.is_empty())
    
    def test_pop(self):
        queue = PriorityQueue()
        queue.add_item('foo', 1)
        queue.add_item('bar', 2)
        queue.add_item(42, 0)

        self.assertEqual(queue.pop(), 42)
        self.assertEqual(queue.pop(), 'foo')
        self.assertEqual(queue.pop(), 'bar')
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
