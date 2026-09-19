import unittest

from metro_graph import build_default_cdmx_metro_map


class MetroGraphTests(unittest.TestCase):
    def setUp(self):
        self.metro = build_default_cdmx_metro_map()

    def test_bfs_finds_shortest_route(self):
        route = self.metro.bfs_route("Observatorio", "Pantitlan")
        self.assertEqual(route, ["Observatorio", "Tacubaya", "Balderas", "Pino Suarez", "Pantitlan"])

    def test_dfs_finds_a_valid_route(self):
        route = self.metro.dfs_route("Observatorio", "Pantitlan")
        self.assertIsNotNone(route)
        self.assertEqual(route[0], "Observatorio")
        self.assertEqual(route[-1], "Pantitlan")

    def test_returns_none_when_station_does_not_exist(self):
        self.assertIsNone(self.metro.bfs_route("NoExiste", "Pantitlan"))
        self.assertIsNone(self.metro.dfs_route("NoExiste", "Pantitlan"))


if __name__ == "__main__":
    unittest.main()
