# 1.查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。

SELECT t_dept.`deptno`"部门编号",dname"部门名称",loc"部门位置",a.cnt"人数"
FROM t_dept, (
	SELECT deptno, COUNT(*) cnt 
	FROM t_employees 
	GROUP BY deptno
	)a 
WHERE t_dept.`deptno`=a.`deptno` ;


# 2.列出所有员工的姓名及其直接上级的姓名。

SELECT t1.ename,t2.ename
FROM t_employees t1,t_employees t2
WHERE t1.MGR=t2.empno 
ORDER BY t2.empno;


# 3.列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。

SELECT t1.ename,t1.hiredate,t2.ename,t2.hiredate
FROM t_employees t1,t_employees t2
WHERE t1.MGR=t2.empno AND t1.hiredate<t2.hiredate
ORDER BY t2.empno;


# 4.列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。

SELECT t_employees.`ename`,t_dept.`deptno`,t_dept.`dname`
FROM t_employees RIGHT OUTER JOIN t_dept 
ON t_employees.deptno=t_dept.deptno
ORDER BY t_dept.`deptno` ;


#5. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。

SELECT job,sal,COUNT(*)
FROM t_employees
GROUP BY job
HAVING MAX(sal)>15000;


#6. 列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。

SELECT t_employees.ename,t_dept.dname
FROM t_employees,t_dept
WHERE t_employees.deptno=(SELECT deptno FROM t_dept WHERE dname='公关部') AND t_dept.deptno=t_employees.deptno;


/*
#7. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
列：* 
表：emp e
条件：sal>(查询出公司的平均工资)
*/
SELECT t1.*,dname,t2.ename
FROM t_employees t1,t_employees t2,t_dept
WHERE t1.sal>(SELECT AVG(sal) FROM t_employees) AND t1.deptno=t_dept.deptno AND t1.MGR=t2.empno;


#8.列出与张飞从事相同工作的所有员工及部门名称。

SELECT t_employees.*, t_dept.dname
FROM t_employees, t_dept
WHERE t_employees.deptno=t_dept.deptno AND job=(SELECT job FROM t_employees WHERE ename='张飞')



/*
#9.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
列：e.ename, e.sal, d.dname
表：emp e, dept d
条件；sal>all (30部门薪金)
*/
SELECT t_employees.ename, t_employees.sal, t_dept.dname
FROM t_employees, t_dept
WHERE t_employees.deptno=t_dept.deptno AND sal > ALL (SELECT sal FROM t_employees WHERE deptno=30)


