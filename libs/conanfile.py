from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake


class ConanLibs(ConanFile):
    name = "conan-libs"
    version = "0.1.0"
    settings = "arch", "build_type", "compiler", "os"
    generators = "VirtualBuildEnv"
    exports_sources = "CMakeLists.txt", "src/*"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        tc.cache_variables["CMAKE_VERBOSE_MAKEFILE:BOOL"] = "ON"
        tc.generate()

        cd = CMakeDeps(self)
        cd.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.set_property("cmake_set_interface_link_directories", "yes")
