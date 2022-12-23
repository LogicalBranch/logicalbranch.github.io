import re, os
from urls import base, articles

# Read the template file
file = open("./redirect.html", "r")
template = file.read().strip()

# Create the redirect files from the template
def write_redirect_file(file_path, redirect):
  os.makedirs(os.path.dirname(file_path), exist_ok = True)
  with open(file_path, "w") as file:
    file.write(template.replace("{redirect}", redirect))

# Create article path variations
def create_article_url_variants(file_path):
  # Create the variants list
  variants = [
    # Nested
    re.sub(".html$", "/index.html", file_path),
    # Hyphenated title
    file_path.replace("_", "-"),
    re.sub(".html$", "/index.html", file_path.replace("_", "-"))
  ]
  # Complex category names
  if "_" in file_path.split("/")[2]:
    # Category with a space
    variants.append(file_path.replace("_", "%20", 1))
    variants.append(re.sub(".html$", "/index.html", variants[-1]))
    # Category with a space and hyphenated title
    variants.append(file_path.replace("_", "%20", 1).replace("_", "-"))
    variants.append(re.sub(".html$", "/index.html", variants[-1]))
  # Return the URL variants
  return variants

# Create base redirect templates
for (file_path, redirect) in base:
  write_redirect_file(file_path, redirect)

# Create article redirect templates
for (f_p, redirect) in articles:
  for file_path in [f_p, *create_article_url_variants(f_p)]:
    write_redirect_file(file_path, redirect)
