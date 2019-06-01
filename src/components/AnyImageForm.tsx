import React from 'react';
import { Form, Row, Col, Input } from 'antd';

class AnyImageForm extends React.Component<any, any> {
  handleSubmit = () => {};
  render() {
    const { getFieldDecorator } = this.props.form;
    return (
      <Form className="ant-advanced-search-form" onSubmit={this.handleSubmit}>
        <Row>
          <Col span={24} style={{ textAlign: 'right' }}>
            <Form.Item label="宽度">
              {getFieldDecorator(`width`, {
                rules: [
                  {
                    required: true,
                    message: '请输入图片宽度',
                  },
                ],
              })(<Input placeholder="placeholder" />)}
            </Form.Item>
          </Col>
        </Row>
      </Form>
    );
  }
}

export default Form.create({ name: 'any_image_form' })(AnyImageForm);
