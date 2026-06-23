import os
import py_compile

errors = []

for root, dirs, files in os.walk("."):

    if "backup" in root:
        continue

    if "__pycache__" in root:
        continue

    for file in files:

        if file.endswith(".py"):

            path = os.path.join(root, file)

            try:

                py_compile.compile(
                    path,
                    doraise=True
                )

            except Exception as e:

                errors.append(
                    f"{path} -> {e}"
                )

if errors:

    print("\nERRORS FOUND\n")

    for err in errors:
        print(err)

else:

    print(
        "\nPROJECT AUDIT PASSED\n"
    )