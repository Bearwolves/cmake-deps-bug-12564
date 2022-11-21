from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake


class ConanApp(ConanFile):
    name = "conan-app"
    version = "0.1.0"
    settings = "arch", "build_type", "compiler", "os"
    generators = "VirtualBuildEnv"
    exports_sources = "CMakeLists.txt", "src/*"
    requires = [
        "conan-libs/0.1.0"
    ]

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
        self.copy("*", src="bin", dst="bin")
