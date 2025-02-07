from conans import ConanFile, CMake


class DriftFrameworkConan(ConanFile):
    name = "reduct-cpp"
    version = "1.3.0"
    license = "MIT"
    author = "Alexey Timin"
    url = "https://github.com/mounte/reduct-cpp"
    description = "Reduct Storage Client SDK for C++"
    topics = ("reduct-storage", "http-client", "http-api")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True, "cpp-httplib:with_openssl": True, "cpp-httplib:with_zlib": True,
                       "date:header_only": True}
    generators = "cmake"

    requires = ("fmt/8.1.1",
                "cpp-httplib/0.10.8",
                "nlohmann_json/3.10.5",
                "openssl/3.0.3",
                "concurrentqueue/1.0.3",
                "date/3.0.1")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run(f'git clone --branch v{self.version} https://github.com/mounte/reduct-cpp.git')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"] = "Release" # Force setting build type for tests...
        cmake.configure(source_dir='reduct-cpp')
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/reduct", src=f"{self.source_folder}/reduct-cpp/src/reduct")
        self.copy("*reductcpp.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["reductcpp"]
