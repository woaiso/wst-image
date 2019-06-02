import React from 'react';
import styles from './index.css';
import { Menu, Icon, Layout, Row, Col } from 'antd';
import AnyImageForm from '@/components/AnyImageForm';
const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;

export default class App extends React.Component<any, any> {
  state = {
    current: 'file-image',
  };

  handleClick = (e: { key: any }) => {
    this.setState({
      current: e.key,
    });
  };
  render() {
    const HelpItem = (
      <span className="submenu-title-wrapper">
        <Icon type="question-circle" />
        帮助
      </span>
    );
    return (
      <Layout>
        <Header className={styles.header}>
        <Menu onClick={this.handleClick} selectedKeys={[this.state.current]} mode="horizontal" className={styles.headerMenu}>
          <Menu.Item key="file-image">
            <Icon type="file-image" />
            生成任意测试图像
          </Menu.Item>
          <Menu.Item key="file-video">
            <Icon type="video-camera" />
            生成任意测试视频
          </Menu.Item>
          <Menu.Item key="edit-image">
            <Icon type="edit" />
            图片格式转换
          </Menu.Item>
          <Menu.Item key="edit-video">
            <Icon type="scissor" />
            视频转换
          </Menu.Item>
          <SubMenu title={HelpItem}>
            <Menu.ItemGroup title="使用说明">
              <Menu.Item key="setting:1">生成任意测试图像</Menu.Item>
              <Menu.Item key="setting:2">生成任意测试视频</Menu.Item>
            </Menu.ItemGroup>
            <Menu.ItemGroup title="常见问题">
              <Menu.Item key="setting:3">图片格式转换</Menu.Item>
              <Menu.Item key="setting:4">视频转换</Menu.Item>
            </Menu.ItemGroup>
          </SubMenu>
          <Menu.Item key="mailto">
            <a href="mailto:woaiso@woaiso.com" rel="noopener noreferrer">
              <Icon type="mail" />
              联系我们
            </a>
          </Menu.Item>
        </Menu>
        </Header>
        <Layout>
          <Content className={styles.content}>
            <Row>
              <Col span={6}><AnyImageForm/></Col>
              <Col span={18}>预览区</Col>
            </Row>
            </Content>
        </Layout>
        <Footer>footer</Footer>
      </Layout>

    );
  }
}
