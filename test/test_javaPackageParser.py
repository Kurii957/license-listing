from unittest import TestCase
import filecmp

from javaPackageParser import JavaPackageParser

class TestJavaPackageParser(TestCase):

    def get_tested_object(self):
        return JavaPackageParser('', '')

    def test_set_version(self):

        res = self.get_tested_object().get_version(':', '1.2.3:compile')
        self.assertEqual('1.2.3', res)

    def test_set_version_with_suffix(self):
        res = self.get_tested_object().get_version(':', '1.2.3.RELEASE:compile')
        self.assertEqual('1.2.3', res)

    def test_set_version_empty(self):
        res = self.get_tested_object().get_version(':', '')
        self.assertEqual('', res)
        
    def test_run(self):
        out_file = 'tmp/java_packages.csv'
        pp = JavaPackageParser('files/dep_tree_out.txt', out_file)
        pp.run()

        self.assertTrue(filecmp.cmp('files/output.csv', out_file));
