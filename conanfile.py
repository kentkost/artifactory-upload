from conans import ConanFile, CMake

class helloWorld(ConanFile):
   name = "HelloWorld"
   version = "1.0"
   description = "Simplpe helloworld that uses boost"
   settings = "os", "compiler", "arch", "build_type"
   options = {"shared": [True, False]}
   default_options = "shared=False"
   generators = "cmake"
   exports_sources = "*"
   #THIS ONE requires = (("boost_spirit/1.66.0@bincrafters/stable", "private"),)
   #requires = ("boost_spirit/1.66.0@bincrafters/stable")
   build_requires= "gtest/1.8.1@bincrafters/stable", "boost_spirit/1.66.0@bincrafters/stable"

   def source(self):
       pass

   def build(self):
       cmake = CMake(self)
       cmake.configure()
       cmake.build()

   def package(self):
       self.copy("Hello/*.h", dst="include", src="src", keep_path=True)
       if self.settings.os == "Windows":
           if self.settings.build_type == "Release":
               self.copy("Hello/Release/Hello.lib", dst="lib", keep_path=False)
           elif self.settings.build_type == "Debug":
               self.copy("Hello/Debug/Hello.lib", dst="lib", keep_path=False)
       else:
           self.copy("Hello/libHello*.a", dst="lib", keep_path=False)

   def package_info(self):
       self.cpp_info.includedirs = ['include']
       self.cpp_info.libdirs = ['lib']
       if self.settings.os == "Windows":
           if self.settings.build_type == "Release":
               self.cpp_info.libs = ["hello.lib"]
           else:
               self.cpp_info.libs = ["hello.lib"]
       else:
           if self.settings.build_type == "Release":
               self.cpp_info.libs = ["libHello.a"]
           else:
               self.cpp_info.libs = ["libHello.a"] 