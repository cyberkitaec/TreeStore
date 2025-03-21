class TreeStore:
    all_items: list[dict[str, any]]
    items: dict[int, dict[str, any]]

    def __init__(self, _items: list[dict[str, any]]) -> None:
        self.all_items = _items
        self.items = {item['id']: item for item in _items}


    def get_all(self) -> list[dict[str, any]]:
        return self.all_items


    def get_item(self, item_id: int) -> dict[str, any]:
        return self.items.get(item_id, None)


    def get_children(self, item_id: int) -> list[dict[str, any]]:
        child_list = [item for item in self.all_items if item.get('parent') == item_id]
        return child_list


    def get_all_parents(self, item_id: int, parent_list: list[dict[str, any]] = None) -> list:

        if parent_list is None:
            parent_list = []

        parent_id = self.items.get(item_id, {}).get('parent')

        if isinstance(parent_id, int):
            parent_list.append(self.get_item(parent_id))
            return self.get_all_parents(parent_id, parent_list)

        return parent_list