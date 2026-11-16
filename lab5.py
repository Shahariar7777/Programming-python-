
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    if not resources:
        print("No resources available.")
        return

    for resource in resources:
        print(resource)


def search_by_category(resources, category):
    found = False

    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True

    if not found:
        print("Category not found.")


def find_unavailable(resources):
    found = False

    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True

    if not found:
        print("All resources are available.")


def search_by_id(resources, resource_id):
    for resource in resources:
        if resource[0] == resource_id:
            print("Resource found:", resource)
            return

    print("Unknown resource ID.")


# Function calls
display_resources(resources)
search_by_id(resources, 999)
search_by_category(resources, "Electronics")
find_unavailable(resources)
