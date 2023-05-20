# программное представление графа в виде словаря, где ключи словаря - вершины графа, а значения словаря - другие словари, где хранятся соседи вершины графа и вес рёбер между ними
graph = {'1': {'2': 1, '3': 5, '4': 4},
         '2': {'1': 1, '5': 7},
         '3': {'1': 5, '5': 2, '6': 7, '7': 2},
         '4': {'1': 4, '6': 3, '7': 3},
         '5': {'2': 7, '3': 2, '8': 7, '9': 8},
         '6': {'3': 6, '4': 3, '9': 7, '10': 3},
         '7': {'3': 2, '4': 3, '9': 4, '10': 3},
         '8': {'5': 7, '11': 5},
         '9': {'5': 8, '6': 7, '11': 5},
         '10': {'6': 3, '7': 6, '11': 3},
         '11': {'8': 5, '9': 5, '10': 3}
         }

# функция кода для нахождения кратчайшего пути и оптимального маршрута между пунктами
def distance(graph, start, end):
    # создание словаря расстояний
    distance = {vertex: float('inf') for vertex in graph}
    # создание словаря предшественников
    previous = {vertex: None for vertex in graph}
    # установка расстояния до начальной точки равное 0
    distance[start] = 0
    # список непосещённых вершин графа
    unvisited = list(graph.keys())

    # пока нашлась непосещённая вершина графа
    while unvisited:
        # нахождение вершины графа с минимальным расстоянием до неё в словаре расстояний
        current_vertex = min(unvisited, key=lambda vertex: distance[vertex])
        # если значение расстояния между двумя вершинами графа найти не удалось, то пропускаем вершины графа
        if distance[current_vertex] == float('inf'):
            break

        # прохождение по всем рёбрам текущей вершины графа
        for neighbor, weight in graph[current_vertex].items():
            # получение кратчайшего пути до соседней вершины графа
            tentative_distance = distance[current_vertex] + weight
            # если он короче, чем уже сохранённое значение
            if tentative_distance < distance[neighbor]:
                # обновление значения расстояния
                distance[neighbor] = tentative_distance
                # обновление предшественника
                previous[neighbor] = current_vertex
        # пометка вершины графа как посещённую
        unvisited.remove(current_vertex)

    # восстановление маршрута
    path, current_vertex = [], end
    while previous[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous[current_vertex]
    if path:
        path.insert(0, current_vertex)
    return distance[end], path

# начальный пункт графа
start = '11'
# конечный пункт графа
end = '1'
# вызов функции кода для нахождения кратчайшего пути и оптимального маршрута между пунктами
distance, path = distance(graph, start, end)
# вывод результата о нахождении кратчайшего пути в графе
print(f'Кратчайшее расстояние от пункта {start} до пункта {end}: {distance}')
# вывод результата о нахождении оптимального маршрута между пунктами
print(f'Оптимальный маршрут от пункта {start} до пункта {end}: {" → ".join(path)}')