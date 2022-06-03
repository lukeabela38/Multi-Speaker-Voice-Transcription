docker run --rm -it \
    -w /workspace \
    -v $PWD/src/:/workspace \
    -p 8000:8000 \
    tvz bash