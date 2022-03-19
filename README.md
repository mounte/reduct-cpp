# Reduct Storage Client SDK for C++

Open source client for [Reduct Storage](https://reduct-storage.dev) written in C++20.

## Features

* Implement Reduct Storage HTTP API v0.3.0
* Support HTTP and HTTPS protocols
* Exception free
* Support Linux AMD64

## Example

```cpp
#include <reduct/client.h>

#include <iostream>

using reduct::IBucket;
using reduct::IClient;

int main() {
  auto client = IClient::Build("http://127.0.0.1:8383");
  // Create a bucket
  auto [bucket, create_err] =
      client->CreateBucket("bucket");
  if (create_err) {
    std::cerr << "Error: " << create_err;
    return -1;
  }

  // Write some data
  IBucket::Time ts = IBucket::Time::clock::now();
  [[maybe_unused]] auto write_err = bucket->Write("entry-1", "some_data1", ts);

  // Read data
  auto [blob, read_err] = bucket->Read("entry-1", ts);
  if (!read_err) {
    std::cout << "Read blob: " <<  blob << std::endl;
  }
}
```

## Build

* GCC 11.2 or higher (support C++20)
* CMake 3.18 or higher
* Conan 1.40 (optional)

```shell
git clone https://github.com/reduct-storage/reduct-cpp.git
cd reduct-cpp
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
sudo cmake --build . --target install
```

cmake tries to use package manager `conan` if it is installed. If it isn't, it downloads all the dependencies by using
FetchContent. To use Reduct Storage SDK you need only to use `find_pacakge` in your cmake lists:

```cmake
find_package(ReductCpp)
```

## References

* [Documentation](https://cpp.reduct-storage.dev)
* [Reduct Storage HTTP API](https://docs.reduct-storage.dev/http-api)