from TreeStore import TreeStore

def main() -> None:
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)

    print(ts.get_all())

    assert ts.get_item(7) == {"id":7,"parent":4,"type":None}


    assert ts.get_children(4) == [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]

    assert ts.get_children(5) == []

    assert ts.get_all_parents(7) ==  [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]


if __name__ == '__main__':
    main()