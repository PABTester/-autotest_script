#!/usr/bin/env/python

# coding = utf-8

import pymysql,inspect

from common.get_log import get_log

class Operate_Mysql():

    def __init__(self, env='fat',log_style='file'):

        self.env = env

        self.log_style = log_style

    def connect_mysql(self):

        if self.env == 'fat':

            connect = pymysql.connect(host='XX.XX.XXX.XXX', port=3306, user='123',

                                      password='XXXXXX', db='数据库名', autocommit=True)

        else:

            connect = pymysql.connect(host='XX.XX.XXX.XXX', port=3306, user='456',

                                      password='XXXXXX', db='数据库名', autocommit=True)

        return connect

    def apply_risk(self, apply_no):

        # 修改数据库的值

        logger = get_log(inspect.stack()[0][3],self.log_style)

        connect = self.connect_mysql()

        cursor = connect.cursor()

        sql = "SELECT `status` from 表明 WHERE apply_no = '%s'" % (apply_no)

        logger.info('执行的sql是:' + sql)

        try:

            cursor.execute(sql)

            risk_status = dict(zip([col[0] for col in cursor.description],[col for col in cursor.fetchone()]))

            content = '结果:' + risk_status['status']

            logger.info(content)

            # if risk_status['status'] != '2':

            #    sql = "UPDATE 表名 SET `status`='%d' WHERE apply_no='%s'" % (2, apply_no)

            #    print('修改值为通过，执行的sql如下：')

            #    try:

            #        cursor.execute(sql)  # 执行sql

            #        connect.commit()  # 提交

            #    except Exception as msg:

            #        print('执行失败，回滚:\n', msg)

            #        connect.rollback()  # 若发生错误回滚

            # else:

            #    print('风险初筛自动审核通过，状态是:', risk_status['status'])

            return risk_status

        except Exception as msg:

            logger.info(msg)

        finally:

            cursor.close()

            connect.close()

    def rabp_apply(self, mchtName):

        """

        查询表数据

        :return: 返回APPLY_NO,

        APPLY_STATUS（1=已提交），

        AUDIT_STATUS = 审核状态(1-待审批 2-审批通过 3-补件 4-拒绝 5-拒绝转补件)

        """

        logger = get_log(inspect.stack()[0][3], self.log_style)

        connect = self.connect_mysql()

        cursor = connect.cursor()

        sql = "SELECT a.APPLY_NO,a.ID_NO,a.license_no,a.MCHT_TYPE,a.BUSINESS_TYPE,a.TRADE_TYPE," \

              "a.APPLY_STATUS,a.AUDIT_STATUS " \

              "from rabp_apply a LEFT JOIN 表名 d ON a.APPLY_NO = d.APPLY_NO WHERE d.MCHT_NAME = '%s';"\

              % (mchtName)

        logger.info('rabp_apply执行的SQL是：' + sql)

        try:

            cursor.execute(sql)

            if cursor.rowcount > 0:

                apply_dict = dict(zip([col[0] for col in cursor.description],[col for col in cursor.fetchall()[-1]]))

                return apply_dict

        except Exception as msg:

            logger.info(msg)

        finally:

            cursor.close()

            connect.close()

    def rabp_approve_node(self, apply_no, approve_node=10):

        """

        :param apply_no:

        :param approve_node: 审批节点 10:风险审核;20:收单审核;30:分期审核;40:风险人工审核

        :return:

        """

        logger = get_log(inspect.stack()[0][3], self.log_style)

        connect = self.connect_mysql()

        cursor = connect.cursor()

        sql = "SELECT r.APPLY_NO,r.approve_step,r.apply_seq,r.approve_status from 表名 r " \

              "WHERE r.APPLY_NO='%s' AND r.approve_node='%s';" % (apply_no,approve_node)

        logger.info('rabp_approve_node执行的SQL是：' + sql)

        try:

            cursor.execute(sql)

            if cursor.rowcount > 0:

                node_dict = dict(zip([col[0] for col in cursor.description],[col for col in cursor.fetchone()]))

                return node_dict

        except Exception as msg:

            print( msg)

        finally:

            cursor.close()

            connect.close()

    def rabp_approve_flow(self, apply_no, approve_node=20,approve_step=1):

        """

        :param apply_no:

        :param approve_node:

        :param approve_step:

        :return: 返回审核节点审核人员UM

        """

        logger = get_log(inspect.stack()[0][3], self.log_style)

        connect = self.connect_mysql()

        cursor = connect.cursor()

        sql = "SELECT a.prev_approve_user from 表名 a " \

              "WHERE a.apply_no='%s' AND a.approve_node='%s' AND a.approve_step='%s'; " \

              % (apply_no,approve_node,approve_step)

        logger.info('rabp_approve_flow执行的SQL是：' + sql)

        try:

            cursor.execute(sql)

            if cursor.rowcount > 0:

                flow_dict = dict(zip([col[0] for col in cursor.description],[col for col in cursor.fetchone()]))

                return flow_dict

        except Exception as msg:

            logger(msg)

        finally:

            cursor.close()

            connect.close()

    def rabp_capital(self,apply_no):

        """ 检查资处审核状态和二录审核人员

        :param apply_no:

        :return:

        """

        logger = get_log(inspect.stack()[0][3], self.log_style)

        connect = self.connect_mysql()

        cursor = connect.cursor()

        sql = "SELECT c.cap_status,c.cap_user,c.qc_status from 表名 c WHERE c.apply_no = '{apply_no}';"\

            .format(apply_no=apply_no)

        logger.info('rabp_capital执行的sql是:' + sql)

        try:

            cursor.execute(sql)

            if cursor.rowcount > 0:

                capital_dict = dict(zip([col[0] for col in cursor.description],[col for col in cursor.fetchall()[-1]]))

                return capital_dict

        except Exception as msg:

            logger.info(msg)

        finally:

            cursor.close()

            connect.close()

if __name__ == '__main__':

    env = 'uat'

    OM = Operate_Mysql(env)

    logger = get_log('rabp', 'console')

    globals()['mchtName'] = 'XXX1'

    apply = OM.rabp_apply(globals()['mchtName'])

    # print(apply)

    # r = OM.rabp_approve_node('0545000020200330164336774344',approve_node=10)

    # print(int(r['approve_step']) == 1 and int(r['approve_status']) == 3)

    # if int(r['approve_step']) == 1 and int(r['approve_status']) == 3:

    #    print('222')

    # r= OM.apply_risk(apply['APPLY_NO'])

    print(apply)
