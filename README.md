# License-listing

Our project is based on writing a program that searches the available projects in order to list dependencies between packages

We want the program to list names, prefixes, versions, licenses, declared licenses, links to licenses and
links to download each package from the selected JAVA project

Before running the program, we will need two files. The first file is a TXT file, while the second is an HTML file.

Once we have them we can start running our program. In order for it to work correctly, we need to specify the path to 
the TXT file and the path to the file where all the information should be saved. Please note that this must be a CSV file

Our program first takes the data from the TXT file and writes all the dependent packages to the CSV file, then it takes 
the information from the HTML file and adds corresponding licenses to the corresponding packages.

The input files look like this:
  TXT file:
  ```
  [INFO] org.springframework.samples:spring-petclinic:jar:2.4.5
  [INFO] +- org.springframework.boot:spring-boot-starter-actuator:jar:2.4.5:compile
  [INFO] |  +- org.springframework.boot:spring-boot-starter:jar:2.4.5:compile
  [INFO] |  |  +- org.springframework.boot:spring-boot-starter-logging:jar:2.4.5:compile
  [INFO] |  |  |  +- ch.qos.logback:logback-classic:jar:1.2.3:compile
  [INFO] |  |  |  |  \- ch.qos.logback:logback-core:jar:1.2.3:compile
  [INFO] |  |  |  +- org.apache.logging.log4j:log4j-to-slf4j:jar:2.13.3:compile
  [INFO] |  |  |  |  \- org.apache.logging.log4j:log4j-api:jar:2.13.3:compile
  ...
  ```
  
  HTML file:
  ```
  <tr class="a">
    <th>GroupId</th>
    <th>ArtifactId</th>
    <th>Version</th>
    <th>Classifier</th>
    <th>Type</th>
    <th>License</th></tr>
  <tr class="b">
    <td>antlr</td>
    <td><a class="externalLink" href="http://www.antlr.org/">antlr</a></td>
    <td>2.7.7</td>
    <td>-</td>
    <td>jar</td>
    <td><a class="externalLink" href="http://www.antlr.org/license.html">BSD License</a></td>
  </tr>
  <tr class="a">
     <td>ch.qos.logback</td>
     <td><a class="externalLink" href="http://logback.qos.ch/logback-access">logback-access</a></td>
     <td>1.2.3</td>
     <td>-</td>
     <td>jar</td>
     <td><a class="externalLink" href="http://www.eclipse.org/legal/epl-v10.html">Eclipse Public License - v 1.0</a></td>
   </tr>
   ```
   
From such input data our program creates CSV file in which data is separated by comma.
CSV file look like that:
  ```
  Package name,Package version,Package name prefix,License type,Declared License
  antlr,2.7.7,antlr,BSD License,BSD-Equivalent
  classmate,1.5.1,com.fasterxml,Apache License Version 2.0,Apache-2.0
  ```
It should be mentioned that all packets are sorted alphabetically regardless of case. 

Thanks to this it is possible to create a table that looks like this:
[Output](https://github.com/Kurii957/license-listing/blob/main/files/output.csv)

For more information click there:
[Wiki](https://github.com/Kurii957/license-listing/wiki)
